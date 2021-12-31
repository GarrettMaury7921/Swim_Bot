import time
import requests
from threading import Thread, Lock


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

    def __init__(self):
        # create a thread lock object
        self.lock = Lock()

    def get_active_deck(self):
        # Listening on Localhost with default runeterra port
        self.active_deck = requests.get(self.address + 'static-decklist')
        return self.active_deck.text

    def get_card_positions(self):
        # Listening on Localhost with default runeterra port
        self.card_positions = requests.get(self.address + 'positional-rectangles')
        return self.card_positions.text

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

            self.active_deck = self.get_active_deck()
            self.card_positions = self.get_card_positions()

            print(self.active_deck)
            print(self.card_positions)

            self.lock.release()

            # Riot says don't query this port for more than 1 second
            time.sleep(1)
