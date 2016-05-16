from BOARD import BOARD_CL
from RGBLED import RGBLED_CL
from BUTTON import BUTTON_CL
import os
import glob
import time

os.system('modprobe w1-therm')
os.system('modprobe w1-gpio')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


class TEMP_CL:
    def __init__(self, BOARD_CL):
        self.board = BOARD_CL
#        self.setup_thermometer()
        self.read_temp_raw()
        self.read_temp(read_temp_raw)
        self.device_file = device_file
    
    def read_temp_raw(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
        
    def read_temp(self, read_temp_raw):
        lines = read_temp_raw()
        print('1')
        while lines[0].strip()[-3:] != 'YES':
                print('2')
                time.sleep(0.2)
                print('3')
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = int(temp_string) / 1000.0
                #temp_f = temp_c * 9 / 5 + 32
                return temp_c
