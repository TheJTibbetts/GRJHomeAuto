from Board import board

class LED_CL:
  def __init__(self, board, pin):
    self.board = board
    self.pin = pin
    self.setup_led()
  
  def setup_led(self):
    self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
  
  def ledOn(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.HIGH)
  
  def ledOff(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.LOW)
