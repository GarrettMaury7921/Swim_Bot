import random
import cv2 as cv
import pyautogui
from time import time, sleep
from libraries import constants1440p, constants1080p, controls
from screen_capturing.window_capture import WindowCapture
from screen_capturing.word_detector import WordDetector


def detect_deck(deck, debug):
    # Loop checkers
    loop_timeout = 0

    # Get deck
    selected_deck = deck

    # Initialize the window capture class
    window_capture = WindowCapture()
    word_detector = WordDetector(selected_deck, debug)

    # Start the threads
    window_capture.start()
    word_detector.start()

    loop_time = time()
    while True:

        # get an updated image of the game
        screenshot = window_capture.screenshot

        # if we don't have a screenshot yet, don't run the code below this point yet
        if screenshot is None:
            continue

        word_detector.update(screenshot)

        sleep(0.07)

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
        if loop_timeout % 20 == 0:
            # Go to the center of the screen and then scroll down
            if controls.get_screensize() == (2560, 1440):
                pyautogui.moveTo(constants1440p.CENTER_DECK_PAGE_X, constants1440p.CENTER_DECK_PAGE_Y, random.random())
                pyautogui.scroll(-30)

        if loop_timeout >= 1000:
            print('Could not find deck...')
            window_capture.stop()
            word_detector.stop()
            exit(-1)

        deck_cords = word_detector.deck_cords
        if deck_cords is not None:
            break

    # Unpack the Tuple
    deck_x, deck_y = deck_cords

    # Click on the selected deck
    pyautogui.moveTo(deck_x, deck_y, random.random())
    pyautogui.leftClick()
    # Stop everything
    word_detector.stop()
    window_capture.stop()
    cv.destroyAllWindows()
