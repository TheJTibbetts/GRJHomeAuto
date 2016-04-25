from LED import LED_CL
from BOARD import BOARD_CL

class RGBLED_CL:
  
  def __init__(self, BOARD_CL, LED_CL):
    self.setup = setup_led
    self.turnOn = ledOn
    self.turnOff = ledOff
    self.pin = pin
    self.board = board
  
  def RLEDsetup(self):
    self.setup
    
  #def GLEDsetup(self):
 #   self.setup
    
  #def BLEDsetup(self):
   # self.setup
  
  def RLEDon(self):
    self.turnOn
  
  #def GLEDon(self):
    #self.turnOn
  
  #def BLEDon(self):
    #self.turnOn

  def RLEDoff(self):
    self.turnOff
  
  #def GLEDoff(self):
    #self.turnOff
  
  #def BLEDoff(self):
  #  self.turnOff

if __name__ == "__main__":
    from BOARD import BOARD_CL
    from LED import LED_CL
    from time import sleep
    rpi = BOARD_CL()
    rled = RGBLED_CL(rpi, 16)
    gled = LED_CL(rpi, 20)
    bled = LED_CL(rpi, 21)
    rled.RLEDon()
    sleep(3)
    rled.RLEDpn()
    gled.ledOn()
    sleep(3)
    gled.ledOff()
    bled.ledOn()
    sleep(3)
    bled.ledOff()
    
