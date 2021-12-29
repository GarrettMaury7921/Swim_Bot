import cv2 as cv
from time import time, sleep
from screen_capturing.window_capture import WindowCapture
from pytesseract import pytesseract
from threading import Thread



def detect_deck(deck, debug):
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
        detect_words(screenshot)

        # resize the windows
        output_image = cv.resize(screenshot, (900, 500))

        if debug is True:
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


def detect_words(screen):
    # Find words in image
    letter_boxes = pytesseract.image_to_boxes(screen)

    height, width, c = screen.shape

    for box in letter_boxes.splitlines():
        box = box.split()
        x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
        cv.rectangle(screen, (x, height-y), (w, height-h), (0, 0, 255), 3)
        cv.putText(screen, box[0], (x, height-h+32), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 0.5)

