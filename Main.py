import RPi.GPIO as GPIO
from LCD import LCD1602_CL
from BUTTON import BUTTON_CL
from LED import LED_CL
from BUZZER import BUZZER_CL
from TEMP import TEMP_CL
from MOTION import MOTION_CL
from pi_Cam import Picture
import time
import os
import glob

#GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

lcd=LCD1602_CL()
tcl=TEMP_CL(4)
led=LED_CL(6, 16, 20)
buzz=BUZZER_CL(6)
mot=MOTION_CL(22)

os.system('modprobe w1-gpio')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

try:

  def clock():
    while True:
      lcd.lcd_string("Clock in GMT", lcd.LCD_LINE_1)
      lcd.lcd_string("now running", lcd.LCD_LINE_2)
      time.sleep(3)
      lcd.lcd_string("-CLOCK-", lcd.LCD_LINE_1)
      lcd.lcd_string(time.strftime("%H" + ":" + "%M" + ":" + "%S"), lcd.LCD_LINE_2)
      time.sleep(0.1)

  def UpDownTemp():
    if GPIO.INPUT(19) == True:
      UpDownTemp =+ 1
    if GPIO.input(26) == True:
      UpDownTemp =- 1

  def temp():
    while True:
      lcd.lcd_string("Temperature", lcd.LCD_LINE_1)
      lcd.lcd_string("now running", lcd.LCD_LINE_2)
      time.sleep(3)
      led.setup_led()
      #GPIO.setup(20, GPIO.OUT)
      #GPIO.setup(16, GPIO.OUT)
      rtemp = int(tcl.read_temp() + UpDownTemp())
      read_string = str(rtemp)
      print(tcl.read_temp())
      lcd.lcd_string("-TEMPERATURE-", lcd.LCD_LINE_1)
      lcd.lcd_string(read_string + " C", lcd.LCD_LINE_2)
      if int(rtemp) >= 24:
        #GPIO.output(16, 1)
        led.ledOnR()
        led.ledOffB()
        #print(read_string)
      elif int(rtemp) < 23.9:
        #GPIO.output(20, 1)
        led.ledOnB()
        led.ledOffR()
        #print(read_string)
      time.sleep(0.1)

  def pirsensor():
    while True:
      lcd.lcd_string("Motion detector", lcd.LCD_LINE_1)
      lcd.lcd_string("now running", lcd.LCD_LINE_2)
      time.sleep(3)
      buzz.setup_buzzer()
      mot.setup_pir()
      #GPIO.setup(22, GPIO.IN)
      #GPIO.setup(5, GPIO.OUT)
      print('setup')
      if GPIO.input(22) == True:
        print ('debug: MOTION DETECTED')
        lcd.lcd_string("MOTION DETECTED", lcd.LCD_LINE_2)
        #os.system('python pi_Cam.py')
        buzz.buzzOn()
        #GPIO.output(5,1)
        time.sleep(1)
        buzz.buzzOff()
        #GPIO.output(5,0)
        time.sleep(1)
      elif GPIO.input(22) == False:
        lcd.lcd_string("", lcd.LCD_LINE_2)
  
  def LED():
    while True:
      lcd.lcd_string("LED dimmer", lcd.LCD_LINE_1)
      lcd.lcd_string("now running", lcd.LCD_LINE_2)
      time.sleep(3)
      led.ledOnW()
  
  def howto():
    lcd.lcd_string("Please read this",lcd.LCD_LINE_1)
    lcd.lcd_string("for help",lcd.LCD_LINE_2)

    time.sleep(3)

    lcd.lcd_string("Button 1:",lcd.LCD_LINE_1)
    lcd.lcd_string("Decrease Temp C",lcd.LCD_LINE_2)

    time.sleep(3)

    lcd.lcd_string("Button 2:",lcd.LCD_LINE_1)
    lcd.lcd_string("Increase Temp C",lcd.LCD_LINE_2)

    time.sleep(3)

    lcd.lcd_string("Button 3:",lcd.LCD_LINE_1)
    lcd.lcd_string("Cycle programs",lcd.LCD_LINE_2)

    time.sleep(3)

    lcd.lcd_string("Button 4:",lcd.LCD_LINE_1)
    lcd.lcd_string("Adjust LED",lcd.LCD_LINE_2)

    time.sleep(3)

  a = ['one', 'two', 'three', 'four', 'five']


  def buttonPressed():
    count = 0
    howto()
    count += 1
    clock()
    count += 1
    temp()
    count += 1
    pirsensor()
    count += 1
    LED()
    if count == 4:
      count = 0

  buttonPressed()

except KeyboardInterrupt:
  lcd.cleanup()
  GPIO.cleanup()
