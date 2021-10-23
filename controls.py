import pyautogui
import time
import constants1080p
from pynput.mouse import Button, Controller


def look_for_main_menu_assets(pic):

    directory = 'image_assets/main_menu/'
    directory = directory + pic

    while 1:
        if pyautogui.locateOnScreen(directory, confidence=.9) is not None:
            print('I can see the ' + pic + ' button!')
            time.sleep(0.4)
            return True
        else:
            print('I cannot see ' + pic)
            return False


def look_for_play_button_assets(pic):

    directory = 'image_assets/play_button/'
    directory = directory + pic

    while 1:
        if pyautogui.locateOnScreen(directory, confidence=.9) is not None:
            print('I can see the ' + pic + ' button!')
            time.sleep(0.4)
            return True
        else:
            print('I cannot see ' + pic)
            return False


def click_home_button():
    pyautogui.moveTo(constants1080p.MOUSE_POSITION_HOME_X, constants1080p.MOUSE_POSITION_HOME_Y)
    pyautogui.leftClick()


def get_cursor_position():
    print('Getting Cursor Position, sleeping 5 seconds')
    time.sleep(5)
    mouse = Controller()
    current_mouse_position = mouse.position
    print(current_mouse_position)
