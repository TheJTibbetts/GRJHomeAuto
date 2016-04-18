import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PIR_PIN = 12
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(5, GPIO.OUT)

def MOTION(PIR_PIN):
#    try:
    while True:
        print 'debug:'+str(GPIO.input(PIR_PIN))
        if GPIO.input(PIR_PIN) == True:    
            print 'debug: MOTION DETECTED'
            GPIO.output(5,1)
            time.sleep(1)
            GPIO.output(5,0)
            time.sleep(1)
        elif GPIO.input(PIR_PIN) == False:
            print 'debug: no motion detected'

#    except:
print 'PIR Module Test (CTRL+C to exit)'
time.sleep(2)
print 'Ready'

#test buzzer
#print('DEBUG: Buzzer on')
#GPIO.output(5, GPIO.HIGH)
#time.sleep(5)
#print('DEBUG: Buzzer off')
#GPIO.output(5, GPIO.LOW)

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(50)
except KeyboardInterrupt:
               print 'Quit'
               GPIO.cleanup()
