from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


def main_menu_starter():
    while 1:
        # MAY CHANGE IF YOU CHANGE COMPUTERS
        # MUST BE SHIFT + (Windows Key) + S FOR SCREENSHOT
        if pyautogui.locateOnScreen('image_assets/main_menu.png', confidence=.9) \
                or pyautogui.locateOnScreen('image_assets/main_menu2.png', confidence=.9) \
                or pyautogui.locateOnScreen('image_assets/main_menu3.png', confidence=.9) is not None:
            print('I can see the main menu!')
            time.sleep(0.5)
            break
        else:
            print('I cannot see it...')
            time.sleep(0.5)
