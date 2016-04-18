import RPi.GPIO
from time import sleep

class board:

    def __init__(self):
        ''' Enables GPIO on Raspberry Pi.
        :param GPIO: RPi.GPIO on the Raspberry Pi
        :param rpi_version: Version of the GPIO library
        :param mode: Current board mode
        :returns none:
        '''

        self.GPIO = RPi.GPIO
        self.setupGpio()
        self.rpi_version = self.GPIO.VERSION
        self.mode = self.GPIO.getmode()

    def setupGpio():
        '''Puts the Raspberry Pi into the correct mode (BCM) and disables warnings.'''

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)

    def print_gpio_details(self):
        '''Prints details of the Raspberry Pi GPIO to the console.'''

        if self.mode == 11:
            mode = 'BCM'
        elif self.mode == 10:
            mode = 'BOARD'
        else:
            mode = 'Error'
        print('Board is set to mode ' + mode)
        print('RPi version is ' + str(self.rpi_version))

    def clean_up(self):
        '''Cleans up assigned GPIO pins on the Raspberry Pi.'''
        
        self.GPIO.cleanup()

if __name__ == "__main__":

    # main program
    rpi = Board()
    rpi.print_gpio_details()
