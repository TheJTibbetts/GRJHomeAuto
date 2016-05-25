import RPi.GPIO as GPIO

class BUZZER_CL:
  def __init__(self, pinB):
    self.pinB = 5
    self.setup_buzzer()
  
  def setup_buzzer(self):
    GPIO.setup(self.pinB, GPIO.OUT)
    GPIO.setwarnings(False)
  
  def buzzOn(self):
    GPIO.output(self.pinB, GPIO.HIGH)
    
  def buzzOff(self):
    GPIO.output(self.pinB, GPIO.LOW)
    
  
if __name__ == "__main__":
    from BOARD import Board
    from time import sleep
    rpi = Board()
    buzz = BUZZER_CL(rpi, 5)
    buzz.buzzerOn()
    sleep(3)
    buzz.buzzerOff()
