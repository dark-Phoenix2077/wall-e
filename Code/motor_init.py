import smbus2, time

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