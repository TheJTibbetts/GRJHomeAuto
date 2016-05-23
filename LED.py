import RPi.GPIO as GPIO
from BOARD import Board


class LED_CL:
  def __init__(self, Board, pinW, pinB, pinR):
    self.board = Board
    self.pinW = 6
    self.pinR = 16
    self.pinB = 20
    self.setup_led()
   
  def setup_led(self, pinW, pinB, pinR):
    GPIO.setup(self.pinW, GPIO.OUT)
    GPIO.setup(self.pinB, GPIO.OUT)
    GPIO.setup(self.pinR, GPIO.OUT)
   
   
   
  def ledOnW(self):
    self.board.GPIO.output(self.pinW, self.board.GPIO.HIGH)
    
  def ledOffW(self):
    self.board.GPIO.output(self.pinW, self.board.GPIO.LOW)
  
  def ledOnR(self):
    self.board.GPIO.output(self.pinR, self.board.GPIO.HIGH)
    
  def ledOffR(self):
    self.board.GPIO.output(self.pinR, self.board.GPIO.LOW)
  
  def ledOnB(self):
    self.board.GPIO.output(self.pinB, self.board.GPIO.HIGH)
    
  def ledOffB(self):
    self.board.GPIO.output(self.pinB, self.board.GPIO.LOW)


# +if __name__ == "__main__":
# +    from BOARD import BOARD_CL
# +    from time import sleep
# +    rpi = BOARD_CL()
# +    led = LED_CL(rpi, 17)
# +    led.ledOn()
# +    sleep(3)
# +    led.ledOff()
