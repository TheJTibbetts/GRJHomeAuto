from BOARD import BOARD_CL
from LCD import LCD1602_CL
from BUTTON import BUTTON_CL
from LED import LED_CL
from BUZZER import BUZZER_CL
from TEMP import TEMP_CL
from MOTION import MOTION_CL

ButtonPresses = [1,2,3,4]

def clock():
  try:
    while True:
      lcd.lcd_string("-CLOCK-", lcd.LCD_LINE_1)
      lcd.lcd_string(time.strftime("%H" + ":" + "%M" + ":" + "%S"), lcd.LCD_LINE_2)
      time.sleep(0.1)
#def temp():
#  try:
#    while True:
#      temp = int(read_temp())
#      read_string = str(temp)
#      print(read_temp())
#      lcd.lcd_string("-TEMPERATURE-", lcd.LCD_LINE_1)
#      lcd.lcd_string(read_string + " C", lcd.LCD_LINE_2)
#      if int(temp) >= 24:
#        GPIO.output(20, 0)
#        GPIO.output(16, 1)
#        #GPIO.output(24, 0)
#      elif int(temp) < 23.9:
#        GPIO.output(20, 1)
#        # GPIO.output(23, 0)
#        GPIO.output(16, 0)
#      time.sleep(0.1)
#def pirsensor():
#  try:
#    while True:
#      print 'debug:'+str(GPIO.input(PIR_PIN))
#      if GPIO.input(PIR_PIN) == True:
#        print 'debug: MOTION DETECTED'
#        lcd.lcd_string("MOTION DETECTED"), lcd.LCD_LINE_2)
#        GPIO.output(5,1)
#        time.sleep(1)
#        GPIO.output(5,0)
#        time.sleep(1)
##Why?      elif GPIO.input(PIR_PIN) == False:
##Why?        print 'debug: no motion detected
