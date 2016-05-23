from time import sleep

class BUTTON_CL:
    def __init__(self, BOARD_CL, 13, 19, 26):
        self.__board = BOARD_CL
        self.__Rpin = 13
        self.__Lpin = 19
        self.__Mpin = 26
        self.__setup_buttonL()
        self.__pressed = False

    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value


    def __setup_buttonL(self, resistor=False):
        if not resistor:
            self.__board.GPIO.setup(self.__Lpin, self.__board.GPIO.IN)
        elif resistor:
            self.__board.GPIO.set(self.__Lpin, self.__board.GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Error setting up resistor')
        
    def __setup_buttonR(self, resistor=False):
        if not resistor:
            self.__board.GPIO.setup(self.__Rpin, self.__board.GPIO.IN)
        elif resistor:
            self.__board.GPIO.set(self.__Rpin, self.__board.GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Error setting up resistor')
        
    def __setup_buttonM(self, resistor=False):
        if not resistor:
            self.__board.GPIO.setup(self.__Mpin, self.__board.GPIO.IN)
        elif resistor:
            self.__board.GPIO.set(self.__Mpin, self.__board.GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Error setting up resistor')
        
        # add interrupt
        self.__board.GPIO.add_event_detect(self.__pin, self.__board.GPIO.FALLING, callback=self.__my_callback, bouncetime=300)
        
    def __my_callback(self, channel):
        self.pressed = True
