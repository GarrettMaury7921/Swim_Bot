import cv2 as cv
from threading import Thread, Lock
from pytesseract import pytesseract, Output


class NumberDetector:

    # threading properties
    stopped = True
    lock = None

    # properties
    screenshot = None
    debug = None
    game_stats = []

    # Path of pytesseract
    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def __init__(self, debug):
        # create a thread lock object
        self.lock = Lock()
        self.debug = debug

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

                # Debugging = Drawing
                if self.debug is True:
                    # Draw rectangles around the words
                    cv.rectangle(self.screenshot, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv.putText(self.screenshot, number, (x, y - 16), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

