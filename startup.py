import pyautogui
import time
import random
from libraries import constants1080p
from libraries import controls


# Looks for Main Menu Runeterra screen
def main_menu_starter():
    while 1:
        # MAY CHANGE IF YOU CHANGE COMPUTERS
        # MUST BE SHIFT + (Windows Key) + S FOR SCREENSHOT
        if pyautogui.locateOnScreen('image_assets/main_menu/main_menu.png', confidence=.9) \
                or pyautogui.locateOnScreen('image_assets/main_menu/main_menu2.png', confidence=.9) \
                or pyautogui.locateOnScreen('image_assets/main_menu/main_menu3.png', confidence=.9) is not None:
            print('I can see the main menu!')
            time.sleep(0.4)
            return True
        else:
            print('I cannot see the main menu...')
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
            return 1  # Break the loop
        else:
            print('Bad Input, try again')
            continue


# When input 1 (Play an AI game) is selected
def play_ai_game():
    print('Click the main menu in 5 seconds, ready to start.')
    time.sleep(5)  # Sleep

    # Move mouse here in (random) seconds
    pyautogui.moveTo(constants1080p.MOUSE_POSITION_PLAY_X, constants1080p.MOUSE_POSITION_PLAY_Y, random.uniform(0.5, 1))
    pyautogui.leftClick()

    time.sleep(0.25)  # Load Time
    controls.look_for_play_button_assets('confirm_play.png')

    while True:
        # Check if Ai button is already selected
        if controls.look_for_play_button_assets('confirm_ai_button.png') is True:
            # time.sleep(0.3)
            # Select Deck
            return True
        elif controls.look_for_play_button_assets('confirm_ai_button.png') is not True:
            pyautogui.moveTo(constants1080p.MOUSE_POSITION_AI_BUTTON_X, constants1080p.MOUSE_POSITION_AI_BUTTON_Y,
                             random.uniform(0.5, 1))
            pyautogui.leftClick()
            return True


# When it is time to select a deck
def deck_selector():
    print('deck time')
