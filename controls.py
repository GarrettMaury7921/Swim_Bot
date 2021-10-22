import pyautogui
import time
import constants1080p


def look_for_main_menu_assets(pic):
    breakout = 0

    directory = 'image_assets/main_menu/'
    directory = directory + pic

    while 1:
        if pyautogui.locateOnScreen(directory, confidence=.9) is not None:
            print('I can see I clicked the ' + pic + ' button!')
            time.sleep(0.4)
            break
        else:
            print('I cannot see it...')
            breakout += 1
            if breakout > 35:
                click_home_button()
                break
            time.sleep(0.4)


def look_for_play_button_assets(pic):
    breakout = 0

    directory = 'image_assets/play_button/'
    directory = directory + pic

    while 1:
        if pyautogui.locateOnScreen(directory, confidence=.9) is not None:
            print('I can see I clicked the ' + pic + ' button!')
            time.sleep(0.4)
            break
        else:
            print('I cannot see it...')
            breakout += 1
            if breakout > 35:
                click_home_button()
                break
            time.sleep(0.4)


def click_home_button():
    pyautogui.moveTo(constants1080p.MOUSE_POSITION_HOME_X, constants1080p.MOUSE_POSITION_HOME_Y)
    pyautogui.leftClick()
