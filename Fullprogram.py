import RPi.GPIO
import time
import os
import glob
import bottle

class Board:
  def __init__(self):
    self.board=RPi.GPIO
    self.setup()
  
  def setup(self):
    self.board.GPIO.setwarning(False)
    self.board.setmode(self.board.BCM)

class TempSense(Board):
  leds = 20, 16
  lcd = LCD1602()
  gpio = RPi.GPIO
  
  gpio.setup(leds, gpio.OUT)
  
  os.system('modprobe w1.gpio')
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
###      
  while True:
    temp = int(read_temp())
    read_string = str(temp)
    print(read_temp())
    lcd.lcd_string("TEMPERATURE: ", lcd.LCD_LINE_1)
    lcd.lcd_string(read_string + "C", lcd.LCD_LINE_2)
    
    if int(temp) >= 24:
      gpio.output(20, 0)
      gpio.output(16, 1)
    
    elif int(temp) < 23.9:
      gpio.output(20, 1)
      gpio.output(16, 0)
    
    time.sleep(0.1)
###

class TempIncrease:
  
class PIR:
  
class Buzzer:
  
class ProtentiousSensor:
  
class ButtonLED:
  
class Menu:
  lcd.lcd_string("Welcome to GRJ", lcd.LCD_LINE_1)
  lcd.lcd_string("HomeAuto System", lcd.LCD_LINE_1)
  

gpio = RPi.GPIO



try:
  
except KeyboardInterrupt:
  lcd.lcd_string("Goodbye!", lcd.LCD_LINE_1)
  time.sleep(3)
  lcd.cleanup()
  gpio.cleanup()
