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

        # Initializes all classes that run with the bot, finds cards, screen capturing and card stats
        self.bot_initializer = Initializer(debug)
        # Stats the thread in the initializer that updates the stats that the card finder finds
        self.bot_initializer.start()
        self.active_deck = ''

        # Sleep to get the other threads to catch up
        time.sleep(3)

        # MULLIGAN HAND CHOOSE CARDS TO KEEP AND THROW AWAY

    # Uses window capturing and number detection to find the health, mana, and spell mana of both players
    def get_health_mana_and_spell_mana(self):
        pass

    # Gets card stats of all cards in play
    def get_card_stats(self):
        while True:

            # all_stats = [my_cards_stats, enemy_cards_stats]
            # all_cards = my_cards, enemy_cards, clean_codes - has x and y values
            all_stats = self.bot_initializer.all_stats
            all_cards = self.bot_initializer.all_cards

            print(all_stats)
            print(all_cards)

    # Prints the player's active deck
    def print_active_deck(self):
        self.active_deck = self.bot_initializer.listener.get_active_deck()
        print(self.active_deck)

