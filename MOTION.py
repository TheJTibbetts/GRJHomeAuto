from BOARD import Board

class MOTION_CL:
    def __init__(self, Board, pin):
        self.__board = Board
        self.__pin = pin
        self.__setup_pir()
        self.__triggered = False

    @property
    def triggered(self):
        return self.__pressed

    @triggered.setter
    def triggered(self, value):
        self.__pressed = value


    def __setup_pir(self, resistor=False):
        if not resistor:
            self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN)
        elif resistor:
            self.__board.GPIO.set(self.__pin, self.__board.GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Pir error')
        
        # add interrupt
        self.__board.GPIO.add_event_detect(self.__pin, self.__board.GPIO.FALLING, callback=self.__my_callback, bouncetime=300)
        
    def __my_callback(self, channel):
        self.pressed = True
