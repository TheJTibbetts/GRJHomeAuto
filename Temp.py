import RPi.GPIO as GPIO
import os
import glob
import time
from lcd1602 import LCD1602

GPIO.setmode(GPIO.BCM)

leds = 20, 16
lcd=LCD1602()

GPIO.setup(leds, GPIO.OUT)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = int(temp_string) / 1000.0
                #temp_f = temp_c * 9 / 5 + 32
                return temp_c
try:
    while True:
            temp = int(read_temp())
            read_string = str(temp)
            print(read_temp())
            lcd.lcd_string("-TEMPERATURE-", lcd.LCD_LINE_1)
            lcd.lcd_string(read_string + "°C", lcd.LCD_LINE_2)
            if int(temp) >= 24:
                GPIO.output(20, 0)
                GPIO.output(16, 1)
                #GPIO.output(24, 0)
            elif int(temp) < 23.9:
                GPIO.output(20, 1)
               # GPIO.output(23, 0)
                GPIO.output(16, 0)
            time.sleep(0.1)

except KeyboardInterrupt:
    lcd.cleanup()
    GPIO.cleanup()
