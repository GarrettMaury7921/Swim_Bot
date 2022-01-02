import time
from bot.card_finder import CardFinder
from port_listening.port_listener import PortListener


class Initializer:

    def __init__(self):
        print('Bot Initializer Started.')
        # Initialize the Card finder first
        card_finder = CardFinder()

        # Initialize the port listener
        listener = PortListener(card_finder)

        listener.start()

        # Wait until we are in game
        print('Waiting for a game to start...')
        while True:
            time.sleep(0.5)
            if '"GameState":"Menus"' in listener.card_positions:
                # Not in game
                continue
            elif '"GameState":"InProgress"' in listener.card_positions:
                # We are in game, start up the bot
                print('Game Started, SWIM_BOT ACTIVATED.')
                break

        # Wait for cards to go in hand
        time.sleep(8.2)
        print('Activating Card Finder.')
        card_finder.start()
