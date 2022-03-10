import time
from threading import Thread, Lock
from bot.card_finder import CardFinder
from port_listening.port_listener import PortListener


class Initializer:
    # threading properties
    stopped = True
    lock = None
    card_finder = None

    def __init__(self, debug):
        # Attributes
        self.debug = debug
        self.all_stats = None
        self.all_cards = None
        # create a thread lock object
        self.lock = Lock()

        print('Bot Initializer Started.')
        # Initialize the Card finder first
        self.card_finder = CardFinder(debug)

        # Initialize the port listener
        listener = PortListener(self.card_finder)

        listener.start()

        # Wait until we are in game
        print('Waiting for a game to start...')
        while True:
            time.sleep(0.5)
            if '"GameState":"Menus"' in listener.card_positions:
                # Not in game
                continue
            elif '"GameState":"InProgress"' in listener.card_positions:
                # We are in game, start up the bot
                print('Game Started, SWIM_BOT ACTIVATED.')
                break

        # Wait for cards to go in hand
        print('Waiting for cards to go in hand...')
        time.sleep(8)
        print('Activating Card Finder.')
        self.card_finder.start()

    # threading methods

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        time.sleep(2)
        print('Activating initializer thread for stats...')
        while not self.stopped:
            # lock the thread while updating the results
            self.lock.acquire()

            # Get the stats from the card_finder to be referenced later in swim_bot
            # Stats have to be present

            # all_stats = [my_cards_stats, enemy_cards_stats]
            self.all_stats = self.card_finder.all_stats
            # all_cards = my_cards, enemy_cards, clean_codes
            self.all_cards = self.card_finder.all_cards

            self.lock.release()
