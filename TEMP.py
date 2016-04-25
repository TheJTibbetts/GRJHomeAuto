from BOARD import BOARD_CL
from RGBLED import RGBLED_CL
from BUTTON import BUTTON_CL
import os
import glob
import time

os.system('modprobe w1-therm')

class TEMP_CL:
    def __init__(self, BOARD_CL, pin):
        self.board = BOARD_CL
        self.pin = pin
#        self.setup_thermometer()
        self.read_temp_raw()
        self.read_temp()
    
    def read_temp_raw(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
        
    def read_temp(self):
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

if __name__ == "__main__":
    from BOARD import BOARD_CL
    from time import sleep
    rpi = BOARD_CL()
    
    try:
        while True:
            temp = int(read_temp())
            read_string = str(temp)
            print(read_temp())
            lcd.lcd_string("-TEMPERATURE-", lcd.LCD_LINE_1)
            lcd.lcd_string(read_string + " C", lcd.LCD_LINE_2)
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
    GPIO.cleanup()
