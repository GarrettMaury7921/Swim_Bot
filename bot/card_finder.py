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
        pass

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
            print(self.positional_rectangles)
            self.lock.release()
