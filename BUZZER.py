from BOARD import Board

class BUZZER_CL:
  def __init__(self, Board, pin):
    self.board = Board
    self.pin = pin
    self.setup_buzzer()
  
  def setup_buzzer(self):
    self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
  
  def buzzerOn(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.HIGH)
    
  def buzzerOff(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.LOW)
    
  
if __name__ == "__main__":
    from BOARD import Board
    from time import sleep
    rpi = Board()
    buzz = BUZZER_CL(rpi, 5)
    buzz.buzzerOn()
    sleep(3)
    buzz.buzzerOff()
