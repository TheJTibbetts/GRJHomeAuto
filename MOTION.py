
import RPi.GPIO as GPIO

class MOTION_CL:
    def __init__(self, pinP):
        self.pinP = 32
        self.setup_pir()
        self.triggered = False

    @property
    def triggered(self):
        return self.pressed

    @triggered.setter
    def triggered(self, value):
        self.pressed = value


    def setup_pir(self, resistor=False):
        if not resistor:
            GPIO.setup(self.pinP, GPIO.IN)
        elif resistor:
            GPIO.set(self.pinP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        else:
            print('Pir error')
        
        # add interrupt
        GPIO.add_event_detect(self.pinP, GPIO.FALLING, callback=self.my_callback, bouncetime=300)
        
    def my_callback(self, channel):
        self.pressed = True
