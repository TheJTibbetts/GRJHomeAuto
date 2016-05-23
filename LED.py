#import RPi.GPIO as GPIO
from BOARD import BOARD_CL
 
class LED_CL:
  def __init__(self, BOARD_CL, pinW, pinB, pinR):
    self.board = BOARD_CL
    self.pinW = 6
    self.pinR = 16
    self.pinB = 20
    self.setup_led()
   
  def setup_led(self):
    self.board.GPIO.setup(self.pinW, self.pinB, self.pinR, self.board.GPIO.OUT)
   
   
   
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
