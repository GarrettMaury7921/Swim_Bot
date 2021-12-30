import random
import cv2 as cv
import pyautogui
from time import time
from screen_capturing.window_capture import WindowCapture
from pytesseract import pytesseract, Output


def detect_deck(deck, debug):
    loop_timeout = 0

    # Get deck
    selected_deck = deck

    # Path of pytesseract
    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # Initialize the window capture class
    window_capture = WindowCapture()

    loop_time = time()
    while True:

        # get an updated image of the game
        screenshot = window_capture.get_screenshot()

        # Detect words in the screenshot to find the deck
        deck_cords = detect_words(screenshot, selected_deck, debug)

        if debug is True:

            # resize the windows
            output_image = cv.resize(screenshot, (900, 500))

            # Display detection image
            cv.imshow('Matches', output_image)

            # debug the loop rate
            print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()

            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            key = cv.waitKey(1)
            if key == ord('q'):
                cv.destroyAllWindows()
                break

        loop_timeout += 1
        if loop_timeout >= 10:
            print('Could not find deck...')
            exit(-1)

        if deck_cords is not None:
            break

    # Unpack the Tuple
    deck_x, deck_y = deck_cords

    # Click on the selected deck
    pyautogui.moveTo(deck_x, deck_y, random.random())
    pyautogui.leftClick()
    cv.destroyAllWindows()


# Detects words on the screen, it detects them easier if the words have spaces in between them
# Meaning you should have multiple words for deck names
def detect_words(screen, selected_deck, debug):

    # Find words in image
    image_data = pytesseract.image_to_data(screen, output_type=Output.DICT)

    for i, word in enumerate(image_data['text']):
        # If the word is all uppercase and doesn't contain any special characters
        if word != "" and word.isupper() and word.isalpha():

            x, y, w, h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]

            # Don't count words that are on the left side of the screen
            if x < 450:
                continue

            # Center Cords for clicking for later
            center_x = (x + (1/2) * w)
            center_y = (y + (1/2) * h)

            # Debugging = Drawing
            if debug is True:
                # Draw a plus where the bot needs to click the deck (center of the word)
                cv.drawMarker(screen, (int(center_x), int(center_y)), (255, 0, 255), cv.MARKER_CROSS, markerSize=40, thickness=2)

                # Draw rectangles around the words
                cv.rectangle(screen, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv.putText(screen, word, (x, y - 16), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            # If the selected deck is found, return the center cords of that deck
            if word == selected_deck:
                return center_x, center_y