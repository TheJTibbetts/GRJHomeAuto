from Board import board

class BUZZER_CL:
  def __init__(self, board, pin):
    self.board = board
    self.pin = pin
    self.setup_buzzer()
  
  def setup_buzzer(self):
    self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
  
  def buzzerOn(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.HIGH)
    
  def buzzerOff(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.LOW)
