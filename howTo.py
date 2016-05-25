from LCD import LCD1602_CL
from time import sleep

lcd = LCD1602_CL()

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

lcd.cleanup()
