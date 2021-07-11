from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(256, 200)[0] == 0:
        click(256, 200)
    if pyautogui.pixel(304, 200)[0] == 0:
        click(304, 200)
    if pyautogui.pixel(358, 200)[0] == 0:
        click(358, 200)
    if pyautogui.pixel(397, 200)[0] == 0:
        click(397, 200)
    