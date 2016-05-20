from BOARD import BOARD_CL
 
class LED_CL:
  def __init__(self, BOARD_CL, pin):
    self.board = BOARD_CL
    self.pin = pin
    self.setup_led()
   
  def setup_led(self):
    self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
   
  def ledOn(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.HIGH)
    
  def ledOff(self):
    self.board.GPIO.output(self.pin, self.board.GPIO.LOW)



 +if __name__ == "__main__":
 +    from BOARD import BOARD_CL
 +    from time import sleep
 +    rpi = BOARD_CL()
 +    led = LED_CL(rpi, 17)
 +    led.ledOn()
 +    sleep(3)
 +    led.ledOff()
