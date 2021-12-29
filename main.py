from menus import Menus
from screen_capturing import text_detection

# This is the main driver code of the bot

initialize_menu = Menus()
if initialize_menu.action == '1':
    # Input in the selected deck, Have True set for debugging (OpenCV Window)
    text_detection.detect_deck(initialize_menu.deck, True)
