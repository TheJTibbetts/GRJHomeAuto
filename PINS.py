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
PIR = 32
Temp = 4
Buzzer = 5
Button_1 = 26
Button_2 = 19
Button_3 = 13
Camera = Dsi
