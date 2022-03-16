import cv2 as cv
from threading import Thread, Lock
from pytesseract import pytesseract, Output
from libraries.controls import get_screensize


class NumberDetector:

    # threading properties
    stopped = True
    lock = None

    # properties
    screenshot = None
    debug = None
    game_stats = []
    screensize = None

    # Path of pytesseract
    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def __init__(self, debug):
        # create a thread lock object
        self.lock = Lock()
        self.debug = debug
        self.screensize = get_screensize()

    # For updating the detector from the window class thread (getting the most recent screenshot)
    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        while not self.stopped:
            if self.screenshot is not None:
                # do object detection
                self.detect_numbers()

                # lock the thread while updating the results
                self.lock.acquire()
                # self.game_stats = stats
                self.lock.release()

    # Detects numbers on the screen
    def detect_numbers(self):
        # Find words in image
        image_data = pytesseract.image_to_data(self.screenshot, output_type=Output.DICT)

        for i, number in enumerate(image_data['text']):
            # If the word is all uppercase and doesn't contain any special characters
            if number != "" and str(number).isdigit():

                x, y, w, h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][
                    i]

                # 2560x1440 setup
                if str(self.screensize) == '(2560, 1440)':
                    # If the data is near the ENEMY HEALTH part of the screen
                    if 341 <= x <= 397 and 512 <= y <= 559:
                        # You can't have more than 20 HP
                        if int(number) <= 20:
                            print('Enemy Health: ' + str(number))

                    # If the data is near the ALLY HEALTH part of the screen
                    if 351 <= x <= 397 and 799 <= y <= 884:
                        if int(number) <= 20:
                            print('Ally Health: ' + str(number))

                    # If the data is near the ENEMY MANA part of the screen
                    if 2099 <= x <= 2151 and 486 <= y <= 533:
                        # No more mana than 10
                        if int(number) <= 10:
                            print('Enemy Mana: ' + str(number))

                    # If the data is near the ALLY MANA part of the screen
                    if 2099 <= x <= 2171 and 825 <= y <= 860:
                        # No more mana than 10
                        if int(number) <= 10:
                            print('Ally Mana: ' + str(number))

                    # HEALTH - TOP LEFT IS WHERE X AND Y IS
                    # enemy
                    # right side down (397, 559)
                    # left side up (361, 522)
                    # ally
                    # right side down (445, 854)
                    # left side up (389, 819)

                    # MANA
                    # left up enemy (2099, 476)
                    # right down enemy (2181, 543)
                    # left up ally (2107, 825)
                    # right down ally (2173, 860)

                    # spell mana
                    # left up enemy (2184, 490)
                    # right down enemy (2214, 527)
                    # up left ally (2182, 918)
                    # up down ally (2216, 949)

                # Debugging = Drawing
                if self.debug is True:
                    # Draw rectangles around the words
                    cv.rectangle(self.screenshot, (x, y), (x + w, y + h), (255, 255, 255), 3)
                    cv.putText(self.screenshot, number, (x, y - 16), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

