from BOARD import BOARD_CL

class LED_CL:
  def __init__(self, BOARD_CL, 6, 16, 20):
    self.board = BOARD_CL
    self.pinW = 6
    self.pinR = 16
    self.pinB = 20
    self.setup_led()
  
  def setup_led(self):
    self.board.GPIO.setup(self.pinW, self.board.GPIO.OUT)
  
  def ledOn(self):
    self.board.GPIO.output(self.pinW, self.board.GPIO.HIGH)
  
  def ledOff(self):
    self.board.GPIO.output(self.pinW, self.board.GPIO.LOW)
    
  def setup_led(self):
    self.board.GPIO.setup(self.pinR, self.board.GPIO.OUT)
  
  def ledOn(self):
    self.board.GPIO.output(self.pinR, self.board.GPIO.HIGH)
  
  def ledOff(self):
    self.board.GPIO.output(self.pinR, self.board.GPIO.LOW)

  def setup_led(self):
    self.board.GPIO.setup(self.pinB, self.board.GPIO.OUT)
  
  def ledOn(self):
    self.board.GPIO.output(self.pinB, self.board.GPIO.HIGH)
  
  def ledOff(self):
    self.board.GPIO.output(self.pinB, self.board.GPIO.LOW)


if __name__ == "__main__":
    from BOARD import BOARD_CL
    from time import sleep
    rpi = BOARD_CL()
    led = LED_CL(rpi, 17)
    led.ledOn()
    sleep(3)
    led.ledOff()
