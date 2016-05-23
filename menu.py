import RPi.GPIO as GPIO
import os
import glob
import time
from LCD import LCD1602_CL
from BUTTON import BUTTON_CL

while True:
    
    count = 0
    btnPress = count + 1
    
    if btnPress == 1:
        run HowTo.py

    if btnPress == 2:
        run Clock.py
    
    if btnPress == 3:
        run Temp.py
    
    if btnPress == 4:
        run Motion.py
    
    if btnPress == 5:
        run Light.py
        count = 0
