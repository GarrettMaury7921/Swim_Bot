from menus import Menus
from screen_capturing import deck_detection
from bot.initializer import Initializer
from bot.swim_bot import Bot

# This is the main driver code of the bot

DEBUGGING = False

# Initialize the resolution and ask the user for an action for the bot to take
# initialize_menu = Menus()
# if initialize_menu.action == '1':
#     # Input in the selected deck, Have True set for debugging (OpenCV Window)
#     deck_detection.detect_deck(initialize_menu.deck, DEBUGGING)

# Initializes all classes that run with the bot, finds cards and card stats
bot_initializer = Initializer(DEBUGGING)
# Stats the thread in the initializer that updates the stats that the card finder finds
bot_initializer.start()

# Put the stats in the swim_bot and initialize the bot script
swim_bot = Bot(bot_initializer, DEBUGGING)
