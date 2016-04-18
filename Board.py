import RPi.GPIO

class Board:
  def __init__(self):
    self.board=RPi.GPIO
    self.setup()
  
  def setup(self):
    self.board.GPIO.setwarning(False)
    self.board.setmode(self.board.BCM)
