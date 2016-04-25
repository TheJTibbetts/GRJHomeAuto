from LED import LED_CL
from BOARD import BOARD_CL

class RGBLED_CL:
  
  def __init__(self, BOARD_CL, LED_CL):
    self.setup = LED_CL.setup_led
    self.turnon = LED_CL.ledOn
    self.turnoff = LED_CL.ledOff
    self.pin = pin
    self.board = board
  
  def RLEDsetup(self):
    self.setup
    
  def GLEDsetup(self):
    self.setup
    
  def BLEDsetup(self):
    self.setup
  
  def RLEDon(self):
    self.turnon
  
  def GLEDon(self):
    self.turnon
  
  def BLEDon(self):
    self.turnon

  def RLEDoff(self):
    self.turnoff
  
  def GLEDoff(self):
    self.turnoff
  
  def BLEDoff(self):
    self.turnoff

if __name__ == "__main__":
    from BOARD import BOARD_CL
    from LED import LED_CL
    from time import sleep
    rpi = BOARD_CL()
    rled = RGBLED_CL(rpi, 16)
    gled = RGBLED_CL(rpi, 20)
    bled = RGBLED_CL(rpi, 21)
    rled.RLEDon()
    sleep(3)
    rled.RLEDoff()
    gled.GLEDon()
    sleep(3)
    gled.GLEDoff()
    bled.BLEDon()
    sleep(3)
    bled.BLEDoff()
    
