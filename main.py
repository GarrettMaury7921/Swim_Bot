from startup import main_menu_starter, _input, play_ai_game, deck_selector
import controls

# Look for the main menu and then prompt the user of what the AI should do
if main_menu_starter() is True:
    # Prompt User
    if _input() is False:  # False = A input has been recognized
        if play_ai_game() is True:  # If everything has gone right
            deck_selector()  # Select A Deck

