from pyautogui import *
import pynput
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4) #This pauses the script for 0.9 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
print ('Welcome to SkipButtonlol')
time.sleep(1) #Delay
print ('Your Skip Hotkey is Alt')
print ('Program will start in 3 seconds')
print ('Questions? Ask @nicks')
print ('...................................')
time.sleep(3) #Delay
print ('Start SkipButtonlol')


count = 0
while count < 5:
    while keyboard.is_pressed('alt') == True:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('skip.png', confidence=0.8)))











            

