from BOARD import BOARD_CL

class PINS_CL:
  def __init__(self, BOARD_CL, pin):
    self.board = BOARD_CL
    self.pin = pin
    self.setup_led()

LED = 6
Rled = 16
Bled = 20
Gled = 21
PIR = 22
Temp = 4
Buzzer = 5
Button_R = 26
Button_L = 19
Button_M = 13
Camera = Dsi
