import RPi.GPIO
from time import sleep

class BOARD_CL:

    def __init__(self):
        self.GPIO = RPi.GPIO
        self.setupGpio()
        self.rpi_version = self.GPIO.VERSION
        self.mode = self.GPIO.getmode()

    def setupGpio(self):
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)

    def clean_up(self):

        self.GPIO.cleanup()
