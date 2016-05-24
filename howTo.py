from lcd1602 import LCD1602
from time import sleep

lcd = LCD1602()

lcd.lcd_string("Please read this",lcd.LCD_LINE_1)
lcd.lcd_string("for help",lcd.LCD_LINE_2)

time.sleep(5)

lcd.lcd_string("Button 1:",lcd.LCD_LINE_1)
lcd.lcd_string("Decrease values",lcd.LCD_LINE_2)

time.sleep(5)

lcd.lcd_string("Button 2:",lcd.LCD_LINE_1)
lcd.lcd_string("Increase value",lcd.LCD_LINE_2)

time.sleep(5)

lcd.lcd_string("Button 3:",lcd.LCD_LINE_1)
lcd.lcd_string("Cycle programs",lcd.LCD_LINE_2)

time.sleep(5)

lcd.lcd_string("Button 4:",lcd.LCD_LINE_1)
lcd.lcd_string("Ajust LED",lcd.LCD_LINE_2)

lcd.cleanup()
