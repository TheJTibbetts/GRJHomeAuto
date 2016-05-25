
import RPi.GPIO as GPIO

class MOTION_CL:
    def __init__(self, pinP):
        self.__pinP = 32
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
            GPIO.setup(self.__pinP, GPIO.IN)
        elif resistor:
            GPIO.set(self.__pinP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Pir error')
        
        # add interrupt
        GPIO.add_event_detect(self.__pinP, GPIO.FALLING, callback=self.__my_callback, bouncetime=300)
        
    def __my_callback(self, channel):
        self.pressed = True
