# ACCESSIBILITY SETTING IN LOR
# Click to Action
import time
from bot.initializer import Initializer


class Bot:

    # Attributes
    bot_initializer = None

    def __init__(self, debug):
        # ALL THREADS CURRENTLY RUNNING
        # - initializer
        # - card finder
        # - port listener

        # Initializes all classes that run with the bot, finds cards and card stats
        self.bot_initializer = Initializer(debug)
        # Stats the thread in the initializer that updates the stats that the card finder finds
        self.bot_initializer.start()
        self.active_deck = ''

        # Sleep to get the other threads to catch up
        time.sleep(3)

    def get_card_stats(self):
        while True:

            # all_stats = [my_cards_stats, enemy_cards_stats]
            # all_cards = my_cards, enemy_cards, clean_codes - has x and y values
            all_stats = self.bot_initializer.all_stats
            all_cards = self.bot_initializer.all_cards

            print(all_stats)
            print(all_cards)

    def print_active_deck(self):
        self.active_deck = self.bot_initializer.listener.get_active_deck()
        print(self.active_deck)

