import time
from threading import Thread, Lock
from bot.card_stat_finder import get_card_stats

# FIND THE CARD CODE OF EACH CARD IN HAND
# SHOWS CARDS IN PLAYER'S HAND IF YOU CAN SEE THEM


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

        # Cut the last end for simple codes, adding to a new variable instead of card for another list
        temp = card[:int(index_to_cut + 1)]

        # Make the first letter of CardCode lowercase for 'card' and 'temp'
        # Using lower() + Put a space after the : + string slicing
        # Lowercase first character of String
        card = ('"' + card[1].lower()) + 'ardCode": ' + card[11:]
        temp = ('"' + temp[1].lower()) + 'ardCode": ' + temp[11:]

        # Fix the last character being an "
        if temp[-1] == '"' and temp[-2] == ',':
            temp = temp[:-1]

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

    # if debug is True:
    #     print('Enemy Cards ' + str(enemy_cards))
    #     print('My Cards ' + str(my_cards))
    #     print('All Card Codes ' + str(clean_codes) + "\n")

    # Return both lists
    return my_cards, enemy_cards, clean_codes


class CardFinder:
    # threading properties
    stopped = True
    lock = None
    positional_rectangles = ''

    # Values have all codes / stats of cards in play
    all_cards = []
    all_stats = []

    def __init__(self, debug):

        # Attributes
        self.debug = debug

        # create a thread lock object
        self.lock = Lock()

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
        print('Finding cards and card stats...')
        while not self.stopped:
            # lock the thread while updating the results
            self.lock.acquire()

            # Get the codes of every card, print them out if we're debugging
            self.all_cards = get_card_codes(self.positional_rectangles)

            # Get the stats of every card from card_stat_finder.py
            self.all_stats = get_card_stats(self.all_cards, self.debug)

            # Getting the cards is so fast, I have to sleep it for a while
            time.sleep(0.2)
            self.lock.release()
