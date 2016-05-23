import RPi.GPIO as GPIO
from BOARD import BOARD_CL
from LCD import LCD1602_CL
#from BUTTON import BUTTON_CL
#from LED import LED_CL
from BUZZER import BUZZER_CL
from TEMP import TEMP_CL
from MOTION import MOTION_CL
import pi_Cam
import time
import os
import glob

GPIO.setmode(GPIO.BCM)

lcd=LCD1602_CL()
tcl=TEMP_CL(4)

os.system('modprobe w1-gpio')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
#ButtonPresses = [1,2,3,4]




#def clock():
#  try:
#    while True:
#      lcd.lcd_string("-CLOCK-", lcd.LCD_LINE_1)
#      lcd.lcd_string(time.strftime("%H" + ":" + "%M" + ":" + "%S"), lcd.LCD_LINE_2)
#      time.sleep(0.1)

##def temp():
#  try:
#    while True:
#      tcl.read_temp_raw()
#      rtemp = int(tcl.read_temp())
#      read_string = str(rtemp)
#      print(tcl.read_temp())
#      lcd.lcd_string("-TEMPERATURE-", lcd.LCD_LINE_1)
#      lcd.lcd_string(read_string + " C", lcd.LCD_LINE_2)
#      if int(rtemp) >= 24:
#        GPIO.output(20, 0)
#        GPIO.output(16, 1)
#      elif int(rtemp) < 23.9:
#        GPIO.output(20, 1)
#        GPIO.output(16, 0)
#      time.sleep(0.1)

def pirsensor():
    try:
        while True:
            GPIO.setup(32, GPIO.IN)
            GPIO.setup(5, GPIO.OUT)
            if GPIO.input(32) == True:
                print ('debug: MOTION DETECTED')
                lcd.lcd_string("MOTION DETECTED", lcd.LCD_LINE_2)
                os.system('python pi_Cam.py')
                GPIO.output(5,1)
                time.sleep(1)
                GPIO.output(5,0)
                time.sleep(1)
            elif GPIO.input(32) == False:
                lcd.lcd_string("", lcd.LCD_LINE_2)


    except KeyboardInterrupt:
        lcd.cleanup()
        GPIO.cleanup()

pirsensor()
