import time
from threading import Thread, Lock


class CardFinder:
    # threading properties
    stopped = True
    lock = None
    positional_rectangles = ''
    card_stats = []

    def __init__(self):
        # create a thread lock object
        self.lock = Lock()

    def get_card_stats(self, positional_rectangles):
        # Get the index of where the word CardID is
        # CardID - 3 is where to start cutting
        index_to_cut = str(positional_rectangles.find('CardID'))
        index_to_cut = int(index_to_cut) - 3
        positional_rectangles = positional_rectangles[int(index_to_cut):]
        print(positional_rectangles)

    # threading methods

    def update_cards(self, positional_rectangles):
        self.lock.acquire()
        self.positional_rectangles = positional_rectangles
        self.lock.release()

        return self.positional_rectangles

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

            # Get the stats of every card
            self.card_stats = self.get_card_stats(self.positional_rectangles)

            # Getting the cards is so fast, I have to sleep it for a while
            time.sleep(0.5)
            self.lock.release()
