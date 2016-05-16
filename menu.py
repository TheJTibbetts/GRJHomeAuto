
import RPi.GPIO as GPIO
import os
import glob
import time
from LCD import LCD1602_CL
from BUTTON import BUTTON_CL

GPIO.setmode(GPIO.BCM)

LCD_menu = []
for i in range(4):
    LCD_menu[i] = {'C', 'T', 'M', 'L'}
    
