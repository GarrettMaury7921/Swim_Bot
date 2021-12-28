import time

import pyautogui
from libraries import controls


class Menus:

    # Attributes
    resolution = 0
    dimensions = ''
    main_menu_dir = 'image_assets/'
    # Different Displays
    monitor1 = (1920, 1080)
    monitor2 = (2560, 1440)

    def __init__(self):
        # Startup Message
        print('----- Swim Bot Activated -----')

        # Initialize Resolution of the main monitor
        self.resolution = controls.get_screensize()
        print(self.get_resolution())

        # Find the main menu
        self.find_main_menu()

    def get_resolution(self):
        if self.resolution == self.monitor2:
            self.dimensions = '2560x1440'

        elif self.resolution == self.monitor1:
            self.dimensions = '1920x1080'
        return 'Resolution Initialized. Resolution is ' + self.dimensions + '.'

    def find_main_menu(self):
        # Update the main menu directory based on the dimensions of the screen
        self.main_menu_dir = self.main_menu_dir + self.dimensions + '/main_menu/main_menu.png'

        while True:
            if pyautogui.locateOnScreen(self.main_menu_dir, confidence=.9) is not None:
                print('Runeterra Main Menu Found.')
                return True
            else:
                print('Trying to find Legends of Runeterra main menu...')
                time.sleep(5)
                continue

