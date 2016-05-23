from BOARD import Board
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
    def __init__(self, Board):
        self.board = Board
#        self.setup_thermometer()
#        self.read_temp_raw()
        self.read_temp()
        self.device_file = device_file
    
#    def read_temp_raw(self):
#        f = open(device_file, 'r')
#        lines = f.readlines()
#        f.close()
#        return lines
        
    def read_temp(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        lines
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = int(temp_string) / 1000.0
                #temp_f = temp_c * 9 / 5 + 32
                return temp_c
