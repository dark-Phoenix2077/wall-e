import cv2
import numpy as np
from camera import Camera
from motor_controller import MotorController


LOWER1 = np.array([0, 120, 70])
UPPER1 = np.array([10, 255, 255])
LOWER2 = np.array([170, 120, 70])
UPPER2 = np.array([180, 255, 255])

TARGET_AREA_MIN = 1000 

def find_target(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, LOWER1, UPPER1)
    mask2 = cv2.inRange(hsv, LOWER2, UPPER2)
    mask = cv2.bitwise_or(mask1, mask2)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None, mask
    
    largest = max(contours, key=cv2.contourArea)
    if cv2.contourArea(largest) < TARGET_AREA_MIN:
        return None, mask
    
    M = cv2.moments(largest)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return (cx, cy, cv2.contourArea(largest)), mask


def run_colour_follow():
    cam = Camera(width=320, height=240)
    motors = MotorController()
    frame_w = 320
    dead_zone = 30 
    
    try:
        while True:
            frame = cam.read()
            if frame is None:
                continue
            
            result, mask = find_target(frame)
            
            if result is None:
                motors.stop()
                motors.steer_centre()
                continue
            
            cx, cy, area = result
            error = cx - (frame_w // 2)
            
            # steering
            if abs(error) < dead_zone:
                motors.steer_centre()
                motors.speed(200)
                motors.forward()
            elif error < 0:
                motors.steer_left()
                motors.speed(150)
                motors.forward()
            else:
                motors.steer_right()
                motors.speed(150)
                motors.forward()
                
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)
            cv2.line(frame, (frame_w//2, 0), (frame_w//2, 240), (255,0,0), 1)
            cv2.putText(frame, f"err: {error}", (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            
            with lock:
                latest_frame = frame.copy()
                
    except KeyboardInterrupt:
        motors.stop()
        cam.release()

run_colour_follow()