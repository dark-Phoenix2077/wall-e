import cv2
import numpy as np
from camera import Camera
from motor_controller import MotorController

def preprocess(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 11, 2)
    return thresh

def find_line_centroid(thresh, roi_start=0.6):
    h, w = thresh.shape
    roi = thresh[int(h * roi_start):, :]
    
    contours, _ = cv2.findContours(roi, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    
    largest = max(contours, key=cv2.contourArea)
    if cv2.contourArea(largest) < 500:
        return None
    
    M = cv2.moments(largest)
    if M['m00'] == 0:
        return None
    cx = int(M['m10'] / M['m00'])
    return cx, w 

def run_line_follow():
    cam = Camera(width=320, height=240)
    motors = MotorController()
    motors.speed(180)
    
    lost_count = 0
    MAX_LOST = 20
    
    try:
        while True:
            frame = cam.read()
            if frame is None:
                continue
            
            thresh = preprocess(frame)
            result = find_line_centroid(thresh)
            
            if result is None:
                lost_count += 1
                if lost_count > MAX_LOST:
                    motors.stop()
                continue
            
            lost_count = 0
            cx, w = result
            error = cx - w // 2
            dead_zone = 25
            
            if abs(error) < dead_zone:
                motors.steer_centre()
                motors.forward()
            elif error < 0:
                motors.steer_left()
                motors.forward()
            else:
                motors.steer_right()
                motors.forward()
            
            cv2.line(frame, (w//2, 0), (w//2, 240), (0,255,0), 1)
            cv2.putText(frame, f"err:{error} lost:{lost_count}",
                        (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                        (255,255,255), 1)
            with lock:
                latest_frame = frame.copy()
                
    except KeyboardInterrupt:
        motors.stop()
        cam.release()