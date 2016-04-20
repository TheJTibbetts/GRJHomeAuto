from LED import LED_CL
from BOARD import BOARD_CL

class RGBLED_CL:
  
  def __init__(self, BOARD_CL, pin, LED_CL):
    self.turnon = ledOn
    self.turnoff = ledOff
    self.board = BOARD_CL
    self.RLEDon()
    self.GLEDon()
    self.BLEDon()
    self.RLEDoff()
    self.GLEDoff()
    self.BLEDoff()
  
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
