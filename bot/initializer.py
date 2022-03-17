import time
import cv2 as cv
from time import time, sleep
from threading import Thread, Lock
from bot.card_finder import CardFinder
from port_listening.port_listener import PortListener
from screen_capturing.window_capture import WindowCapture
from screen_capturing.number_detector import NumberDetector


class Initializer:
    # threading properties
    stopped = True
    lock = None

    def __init__(self, debug):
        # Attributes
        self.debug = debug
        self.all_stats = ''
        self.all_cards = ''
        self.card_finder = None
        # create a thread lock object
        self.lock = Lock()

        print('Bot Initializer Started.')
        # Initialize the Card finder first
        self.card_finder = CardFinder(debug)

        # Initialize and start the port listener
        self.listener = PortListener(self.card_finder)
        self.listener.start()

        # Initialize the window capture class
        self.screenshot = None
        self.window_capture = WindowCapture()

        # Initialize the number detector class
        self.number_detector = NumberDetector(self.debug)

        # Wait until we are in game
        print('Waiting for a game to start...')
        while True:
            sleep(0.5)
            if '"GameState":"Menus"' in self.listener.card_positions:
                # Not in game
                continue
            elif '"GameState":"InProgress"' in self.listener.card_positions:
                # We are in game, start up the bot
                print('Game Started, SWIM_BOT ACTIVATED.')
                break

        # Wait for cards to go in hand
        print('Waiting for cards to go in hand...')
        sleep(8)
        print('Activating Card Finder.')
        self.card_finder.start()
        print('Activating Window Capturing.')
        self.window_capture.start()

        # Wait for the window capture to catch up
        sleep(3)
        # Start the number detector
        print('Activating Number Detector.')
        self.number_detector.start()

    # threading methods

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        sleep(2)
        loop_time = time()
        print('Activating initializer thread for stats...')
        while not self.stopped:
            # lock the thread while updating the results
            self.lock.acquire()

            # Get the stats from the card_finder to be referenced later in swim_bot
            # Stats have to be present

            # all_stats = [my_cards_stats, enemy_cards_stats]
            self.all_stats = self.card_finder.all_stats
            # print(self.all_stats)

            # all_cards = my_cards, enemy_cards, clean_codes
            self.all_cards = self.card_finder.all_cards
            # print(self.all_cards)

            # WINDOW CAPTURE -- Get the current screenshot
            self.screenshot = self.window_capture.screenshot
            # Convert to Grayscale and then black and white
            self.screenshot = cv.cvtColor(self.screenshot, cv.COLOR_BGR2GRAY)
            # Notes: For Health and Spell Mana, 200 is good
            # All round: 191 is ok
            thresh, image_black = cv.threshold(self.screenshot, 191, 255, cv.THRESH_BINARY)
            self.screenshot = image_black

            # Keep the number detector updated with the latest screenshot
            self.number_detector.update(self.screenshot)

            # if we don't have a screenshot yet, don't run the code below this point yet
            if self.screenshot is None:
                # RACE CONDITION - TRY ON OTHER COMP
                sleep(0.3)
                self.lock.release()
                continue

            # Sleep for a little bit to give the detector time to update and find the numbers
            # Toying with this number can either make the output look like it's skipping or look more accurate
            # ^ Mostly because it is probably moving too fast in terms of fps
            sleep(0.2)

            # IF TRUE: Show output on a separate screen
            if self.debug is True:

                # resize the windows
                output_image = cv.resize(self.screenshot, (900, 500))

                # Display detection image
                cv.imshow('Matches', output_image)

                # debug the loop rate
                # print('(Reduced from sleeping) FPS {}'.format(1 / (time() - loop_time)))
                loop_time = time()

                # press 'q' with the output window focused to exit.
                # waits 1 ms every loop to process key presses
                key = cv.waitKey(1)
                if key == ord('q'):
                    cv.destroyAllWindows()
                    break

            # RACE CONDITION - TRY ON OTHER COMP
            sleep(0.3)
            self.lock.release()
