import time
import requests
from threading import Thread, Lock
from bot.card_finder import CardFinder


class PortListener:

    # threading properties
    stopped = True
    lock = None

    # Attributes
    ip = '127.0.0.1'
    port = 21337
    address = 'http://' + ip + ':' + str(port) + '/'

    active_deck = ''
    card_positions = ''
    game_result = ''

    card_finder = None

    def __init__(self, card_finder):
        # create a thread lock object
        self.lock = Lock()

        # Get the card finder
        self.card_finder = card_finder

    def get_active_deck(self):
        # Listening on Localhost with default runeterra port
        self.active_deck = requests.get(self.address + 'static-decklist')
        return self.active_deck.text

    def get_card_positions(self):
        # Listening on Localhost with default runeterra port
        self.card_positions = requests.get(self.address + 'positional-rectangles')
        return self.card_positions.text

    def get_game_result(self):
        self.game_result = requests.get(self.address + 'game-result')
        return self.game_result.text

    # threading methods

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        while not self.stopped:

            # lock the thread while updating the results
            self.lock.acquire()

            # Get all of the data from the port
            self.active_deck = self.get_active_deck()
            self.card_positions = self.get_card_positions()
            self.game_result = self.get_game_result()

            # Update card positions in the finder
            self.card_finder.update_cards(self.card_positions)

            # print(self.active_deck)
            # print(self.card_positions)

            self.lock.release()

            # Riot says don't query this port for more than 1 second
            time.sleep(1)
