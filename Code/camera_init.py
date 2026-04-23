import cv2


class Camera:
    def __init__(self, index=0, width=640, height=480):
        self.cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def read(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        self.cap.release()

class MotorController:
    ADDR = 0x10
    
    def __init__(self):
        self.bus = smbus2.SMBus(1)
    
    def _send(self, cmd):
        self.bus.write_byte(self.ADDR, ord(cmd))
    
    def forward(self):  self._send('F')
    def backward(self): self._send('B')
    def stop(self):     self._send('S')
    def steer_left(self):   self._send('L')
    def steer_right(self):  self._send('R')
    def steer_centre(self): self._send('C')
    
    def speed(self, val):
        val = max(0, min(255, int(val)))
        self.bus.write_byte(self.ADDR, ord('X'))
        self.bus.write_byte(self.ADDR, val)