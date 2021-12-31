import random
import time
import pyautogui
from libraries import controls, constants1080p, constants1440p


class Menus:

    # Different Display Constants
    monitor1 = (1920, 1080)
    monitor2 = (2560, 1440)

    # Attributes
    action = 0
    deck = ''
    resolution = 0
    dimensions = ''
    main_menu_dir = 'image_assets/'

    def __init__(self):
        # Startup Message
        print('----- Swim Bot Activated -----')

        # Initialize Resolution of the main monitor
        self.resolution = controls.get_screensize()
        print(self.get_resolution())

        # Find the main menu
        self.find_main_menu()

        # Select Action for the bot to take
        self.take_action()

    def get_resolution(self):
        if self.resolution == self.monitor2:
            self.dimensions = '2560x1440'

        elif self.resolution == self.monitor1:
            self.dimensions = '1920x1080'
        return 'Resolution Initialized. Resolution is ' + self.dimensions + '.'

    def find_main_menu(self):
        # Variable for tracking if the main menu has not been found yet
        menu_finder = False

        # Update the main menu directory based on the dimensions of the screen
        # image_assets/*dimensions*/main_menu/main_menu.png
        main_menu_settings = self.main_menu_dir + self.dimensions + '/main_menu/main_menu3.png'
        self.main_menu_dir = self.main_menu_dir + self.dimensions + '/main_menu/main_menu.png'

        while True:
            # Checks to see if the main menu can be found by looking if components of the menu are on screen
            if pyautogui.locateOnScreen(self.main_menu_dir, confidence=.9) is not None and \
                    pyautogui.locateOnScreen(main_menu_settings, confidence=.9) is not None:
                print('Runeterra Main Menu Found.')
                return True
            else:
                if menu_finder is True:
                    print('.', end='')
                    time.sleep(1)
                    continue

                print('Trying to find Legends of Runeterra main menu...', end='')

                # Main menu has not been found yet, now put . at the end of the print statement
                menu_finder = True

                time.sleep(0.3)
                continue

    def take_action(self):
        print('Select an Action:')
        self.action = input('1. AI Game\n')
        if int(self.action) == 1:
            self.deck = input('What deck should I play? (Type in the name of the deck here)\n')

            print('Please Click on the Runeterra Client.')
            print('Playing AI Game...')
            time.sleep(2)
            self.go_to_ai_game(self.dimensions)
            return 1

    @staticmethod
    def go_to_ai_game(dimensions):
        if str(dimensions) == '1920x1080':
            # Click on Play Button
            pyautogui.moveTo(constants1080p.MOUSE_POSITION_PLAY_X,
                             constants1080p.MOUSE_POSITION_PLAY_Y, random.random())
            pyautogui.leftClick()

            # Click on AI Button
            pyautogui.moveTo(constants1080p.MOUSE_POSITION_AI_BUTTON_X,
                             constants1080p.MOUSE_POSITION_AI_BUTTON_Y, random.random())
            pyautogui.leftClick()
        elif str(dimensions) == '2560x1440':
            # Click on Play Button
            pyautogui.moveTo(constants1440p.MOUSE_POSITION_PLAY_X,
                             constants1440p.MOUSE_POSITION_PLAY_Y, random.random())
            pyautogui.leftClick()

            # Sleep for a small amount due to clicks not happening sometimes
            time.sleep(0.2)

            # Click on AI Button
            pyautogui.moveTo(constants1440p.MOUSE_POSITION_AI_BUTTON_X,
                             constants1440p.MOUSE_POSITION_AI_BUTTON_Y, random.random())
            pyautogui.leftClick()
