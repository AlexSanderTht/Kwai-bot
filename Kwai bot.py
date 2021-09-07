# Kwai-bot
#In this project the phone's screen mirroring was used and every pixel coordinate for automation.

import pyautogui            
import time

for i in range(500):
    pyautogui.moveTo(300,652)
    pyautogui.mouseDown()
    pyautogui.moveTo(308,115)
    pyautogui.mouseUp()
    time.sleep(10.0)
