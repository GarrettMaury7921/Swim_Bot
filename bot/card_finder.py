import sys
import time
from threading import Thread, Lock


# FIND THE CARD CODE OF EACH CARD IN HAND
def get_card_codes(positional_rectangles):

    # Get the index of where the word 'CardID' is
    # CardID - 3 is where to start cutting
    index_to_cut = str(positional_rectangles.find('CardID'))
    index_to_cut = int(index_to_cut) - 3
    positional_rectangles = positional_rectangles[int(index_to_cut):]

    # Getting rid of unneeded parts of string
    temp = 0
    counter = 0
    # Cycles through two unneeded values from port, two are 'face' cards that are just the top cards of the player's
    # decks -- We skip this ^
    for characters in positional_rectangles:
        counter += 1
        if '}' in characters:
            temp += 1
        if temp == 2:
            temp = counter
            break
    # Temp + 1 = the first card seen
    temp += 1
    # Format the cards
    positional_rectangles = positional_rectangles[temp:]
    cards = str(positional_rectangles).split("},{")

    # ** Get the Card Codes **
    index = 0
    card_codes = []
    # For just the codes and no extra info
    clean_codes = []
    for card in cards:
        # Find the 'CardCode' keyword and cut everything before and after the code so it's just the card code
        index_to_cut = cards[index].find('CardCode')
        # -1 because it should include the ""
        index_to_cut -= 1
        card = card[int(index_to_cut):]

        # Fix the last character not being a "
        if card[-1] != '"':
            card = card + '"'

        # Cut the last end for simple codes, adding to a new variable instead of card for another list
        temp = card[:int(index_to_cut)]

        # add the cards to the whole list
        card_codes.append(card)
        clean_codes.append(temp)

        index += 1

    # Check if all cards are local player or not and add them to their own lists
    my_cards = []
    enemy_cards = []
    for x in range(len(card_codes)):
        # print(card_codes[x])
        # Add my own cards to the lists
        if "true" in card_codes[x]:
            my_cards.append(card_codes[x])

        # If a card belongs to the enemy, add it to the lists
        if "false" in card_codes[x]:
            enemy_cards.append(card_codes[x])

    # print(enemy_cards)
    # print(my_cards)
    # print(clean_codes)

    # Return both lists
    return my_cards, enemy_cards, clean_codes


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

    # SHOWS CARDS IN PLAYER'S HAND IF YOU CAN SEE THEM

    def get_card_stats(self):
        # Open the files needed to search through to find the stats for each card in your hand
        file1 = open(self.set1, "r")
        file2 = open(self.set2, "r")
        file3 = open(self.set3, "r")
        file4 = open(self.set4, "r")
        file5 = open(self.set5, "r")

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
            self.card_stats = get_card_codes(self.positional_rectangles)

            # Getting the cards is so fast, I have to sleep it for a while
            time.sleep(0.5)
            self.lock.release()
