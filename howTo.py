from lcd1602 import LCD1602
from time import sleep

lcd = LCD1602()

lcd.lcd_string("Please hold for",lcd.LCD_LINE_1)
lcd.lcd_string("help...",lcd.LCD_LINE_2)

time.sleep(5)

lcd.lcd_string("To continue to",lcd.LCD_LINE_1)
lcd.lcd_string("the next ",lcd.LCD_LINE_2)



lcd.lcd_string("To start press",lcd.LCD_LINE_1)
lcd.lcd_string("button 3",lcd.LCD_LINE_2)
