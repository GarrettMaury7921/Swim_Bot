import sys
import time
from threading import Thread, Lock


class CardFinder:
    # threading properties
    stopped = True
    lock = None
    positional_rectangles = ''
    card_stats = []

    # File Variables
    set1 = sys.path[0] + "/bot/card_assets/set1-en_us.json"
    set2 = sys.path[0] + "/bot/card_assets/set2-en_us.json"
    set3 = sys.path[0] + "/bot/card_assets/set3-en_us.json"
    set4 = sys.path[0] + "/bot/card_assets/set4-en_us.json"
    set5 = sys.path[0] + "/bot/card_assets/set5-en_us.json"

    def __init__(self):
        # create a thread lock object
        self.lock = Lock()

    def get_card_codes(self, positional_rectangles):
        # FIND THE CARD CODE OF EACH CARD IN HAND

        # Get the index of where the word CardID is
        # CardID - 3 is where to start cutting
        index_to_cut = str(positional_rectangles.find('CardID'))
        index_to_cut = int(index_to_cut) - 3
        positional_rectangles = positional_rectangles[int(index_to_cut):]

        # Getting rid of unneeded parts of string
        temp = 0
        counter = 0
        for characters in positional_rectangles:
            counter += 1
            if '}' in characters:
                temp += 1
            if temp == 2:
                temp = counter
                break
        # Temp + 1 = the first card seen
        temp += 1
        positional_rectangles = positional_rectangles[temp:]
        # Get the cards in a dictionary
        cards = str(positional_rectangles).split("},{")

        # Get the Card Codes
        index = 0
        card_codes = []
        for card in cards:
            index_to_cut = cards[index].find('CardCode')
            # -1 because it should include the ""
            index_to_cut -= 1

            # Cut everything before and after the code so it's just the card code
            card = card[int(index_to_cut):]
            card = card[:int(index_to_cut)]

            # Fix the last character not being a "
            if card[-1] != '"':
                card = card + '"'

            # Change the cards
            card_codes.append(card)

            index += 1

        # Open the files needed to search through to find the stats for each card in your hand
        file1 = open(self.set1, "r")
        file2 = open(self.set2, "r")
        file3 = open(self.set3, "r")
        file4 = open(self.set4, "r")
        file5 = open(self.set5, "r")
        print(card_codes)

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
            self.card_stats = self.get_card_codes(self.positional_rectangles)

            # Getting the cards is so fast, I have to sleep it for a while
            time.sleep(0.5)
            self.lock.release()
