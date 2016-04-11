mport os
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
device_file = device_folder
