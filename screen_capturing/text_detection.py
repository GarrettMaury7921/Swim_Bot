import cv2 as cv
from time import time, sleep
from screen_capturing.window_capture import WindowCapture


def detect_deck(deck):
    # Get deck
    selected_deck = deck

    # Initialize the window capture class
    window_capture = WindowCapture()

    loop_time = time()
    while True:

        # get an updated image of the game
        screenshot = window_capture.get_screenshot()

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
