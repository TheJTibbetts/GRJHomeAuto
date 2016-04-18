import RPi.GPIO as GPIO
import os
import glob
import time
from lcd1602 import LCD1602

GPIO.setmode(GPIO.BCM)

lcd=LCD1602()

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

try:
        while True:
                lcd.lcd_string("-CLOCK-", lcd.LCD_LINE_1)
                lcd.lcd_string(time.strftime("%H" + ":" + "%M" + ":" + "%S"), lcd.LCD_LINE_2)
                time.sleep(0.1)

except KeyboardInterrupt:
    lcd.cleanup()
    GPIO.cleanup()
