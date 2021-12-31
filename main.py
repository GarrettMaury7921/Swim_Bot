from menus import Menus
from screen_capturing import deck_detection

# This is the main driver code of the bot


# Initialize the resolution and ask the user for an action for the bot to take
initialize_menu = Menus()
if initialize_menu.action == '1':
    # Input in the selected deck, Have True set for debugging (OpenCV Window)
    deck_detection.detect_deck(initialize_menu.deck, False)
