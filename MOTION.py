from BOARD import BOARD_CL
from BUZZER import BUZZER_CL

class Motion_CL:
  def __init__(self, BOARD_CL):
    self.board = BOARD_CL
    self.buzzer = BUZZER_CL
    self.pin = pin
    self.setup_PIR

if __name__ == "__main__":
    from BOARD import BOARD_CL
    from time import sleep
    rpi = BOARD_CL()
    mot = Motion_CL(rpi, 17)
    mot.buzzerOn()
    sleep(1)
    mot.buzzerOff()
