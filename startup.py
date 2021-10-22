from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
from pynput.mouse import Button, Controller
# Example print(constants1080p.MOUSE)
import constants1080p
import controls


# Looks for Main Menu Runeterra screen
def main_menu_starter():
    while 1:
        # MAY CHANGE IF YOU CHANGE COMPUTERS
        # MUST BE SHIFT + (Windows Key) + S FOR SCREENSHOT
        if pyautogui.locateOnScreen('image_assets/main_menu/main_menu.png', confidence=.9) \
                or pyautogui.locateOnScreen('image_assets/main_menu/main_menu2.png', confidence=.9) \
                or pyautogui.locateOnScreen('image_assets/main_menu/main_menu3.png', confidence=.9) is not None:
            print('I can see the main menu!')
            _input()  # Await for input from the user
            time.sleep(0.4)
            break
        else:
            print('I cannot see it...')
            time.sleep(0.4)


# After the main menu has been found, it asks the user for some input of what to do
def _input():
    loop = True
    while loop:
        # Should give some seconds for user to click on screen so ai doesn't get confused
        print('Awaiting Input...')
        print('1. Play an AI game')
        cmdinput = input()
        if cmdinput == '1':
            print('Sleeping for 5, click the main menu...')
            play_ai_game()
            loop = False  # Break the loop, a decision has been made
        else:
            print('Bad Input, try again')
            continue


# When input 1 (Play an AI game) is selected
def play_ai_game():
    time.sleep(5)  # Sleep for 5

    pyautogui.moveTo(constants1080p.MOUSE_POSITION_PLAY_X, constants1080p.MOUSE_POSITION_PLAY_Y)
    pyautogui.leftClick()

    time.sleep(0.25)  # Load Time
    controls.look_for_play_button_assets('confirm_play.png')
