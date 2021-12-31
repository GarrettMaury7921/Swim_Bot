import cv2 as cv
from threading import Thread, Lock
from pytesseract import pytesseract, Output


class WordDetector:

    # threading properties
    stopped = True
    lock = None

    # properties
    selected_deck = None
    screenshot = None
    debug = None
    deck_cords = None

    # Path of pytesseract
    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def __init__(self, selected_deck, debug):
        # create a thread lock object
        self.lock = Lock()
        # load the trained model
        self.selected_deck = selected_deck
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
                deck_cords = self.detect_words()
                # lock the thread while updating the results
                self.lock.acquire()
                self.deck_cords = deck_cords
                self.lock.release()

    # Detects words on the screen, it detects them easier if the words have spaces in between them
    # Meaning you should have multiple words for deck names
    def detect_words(self):
        # Find words in image
        image_data = pytesseract.image_to_data(self.screenshot, output_type=Output.DICT)

        for i, word in enumerate(image_data['text']):
            # If the word is all uppercase and doesn't contain any special characters
            if word != "" and word.isupper() and word.isalpha():

                x, y, w, h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][
                    i]

                # Don't count words that are on the left side of the screen
                if x < 450:
                    continue

                # Center Cords for clicking for later
                center_x = (x + (1 / 2) * w)
                center_y = (y + (1 / 2) * h)

                # Debugging = Drawing
                if self.debug is True:
                    # Draw a plus where the bot needs to click the deck (center of the word)
                    cv.drawMarker(self.screenshot, (int(center_x), int(center_y)), (255, 0, 255), cv.MARKER_CROSS,
                                  markerSize=40, thickness=2)

                    # Draw rectangles around the words
                    cv.rectangle(self.screenshot, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv.putText(self.screenshot, word, (x, y - 16), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

                # If the selected deck is found, return the center cords of that deck
                if word == self.selected_deck:
                    return center_x, center_y
