import RPi.GPIO as GPIO
from BOARD import Board


class LED_CL:
  def __init__(self, Board, pinW, pinB, pinR):
    self.board = Board
    self.pinW = 6
    self.pinR = 16
    self.pinB = 20
    self.setup_led()
   
  def setup_led(self):
    GPIO.setup(self.pinW, GPIO.OUT)
    GPIO.setup(self.pinB, GPIO.OUT)
    GPIO.setup(self.pinR, GPIO.OUT)
   
   
   
  def ledOnW(self):
    GPIO.output(self.pinW, GPIO.HIGH)
    
  def ledOffW(self):
    GPIO.output(self.pinW, GPIO.LOW)
  
  def ledOnR(self):
    GPIO.output(self.pinR, GPIO.HIGH)
    
  def ledOffR(self):
    GPIO.output(self.pinR, GPIO.LOW)
  
  def ledOnB(self):
    GPIO.output(self.pinB, GPIO.HIGH)
    
  def ledOffB(self):
    GPIO.output(self.pinB, GPIO.LOW)


# +if __name__ == "__main__":
# +    from BOARD import BOARD_CL
# +    from time import sleep
# +    rpi = BOARD_CL()
# +    led = LED_CL(rpi, 17)
# +    led.ledOn()
# +    sleep(3)
# +    led.ledOff()
