from BOARD import BOARD_CL

class BUZZER_CL:
  def __init__(self, BOARD_CL, pin):
    self.board = BOARD_CL
    self.pin = pin
    self.setup_buzzer()
  
  def setup_buzzer(self):
    self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
  
  def buzzerOn(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.HIGH)
    
  def buzzerOff(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.LOW)
    
  
if __name__ == "__main__":
    from BOARD import BOARD_CL
    from time import sleep
    rpi = BOARD_CL()
    buzz = BUZZER_CL(rpi, 5)
    buzz.buzzerOn()
    sleep(3)
    buzz.buzzerOff()
