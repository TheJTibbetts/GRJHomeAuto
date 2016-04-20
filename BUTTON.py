from time import sleep

class BUTTON_CL:
    def __init__(self, BOARD_CL, pin):
        self.__board = BOARD_CL
        self.__pin = pin
        self.__setup_button()
        self.__pressed = False

    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value


    def __setup_button(self, resistor=False):
        if not resistor:
            self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN)
        elif resistor:
            self.__board.GPIO.set(self.__pin, self.__board.GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Error setting up resistor')
        
        # add interrupt
        self.__board.GPIO.add_event_detect(self.__pin, self.__board.GPIO.FALLING, callback=self.__my_callback, bouncetime=300)
        
    def __my_callback(self, channel):
        self.pressed = True
