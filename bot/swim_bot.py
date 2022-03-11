# ACCESSIBILITY SETTING IN LOR
# Click to Action
import time
from bot.initializer import Initializer


class Bot:

    # Attributes
    bot_initializer = None

    def __init__(self, debug):
        # Initializes all classes that run with the bot, finds cards and card stats
        self.bot_initializer = Initializer(debug)
        # Stats the thread in the initializer that updates the stats that the card finder finds
        self.bot_initializer.start()

        time.sleep(3)

        # while True:

            # all_stats = [my_cards_stats, enemy_cards_stats]
            # all_cards = my_cards, enemy_cards, clean_codes - has x and y values

            # print(str(self.bot_initializer.all_stats))
            # print(str(self.bot_initializer.all_cards))
