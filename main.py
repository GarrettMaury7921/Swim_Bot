from startup import main_menu_starter, _input, play_ai_game, deck_selector


def ai_game():
    # Look for the main menu and then prompt the user of what the AI should do
    if main_menu_starter() is True:
        if play_ai_game() is True:  # If everything has gone right
            deck_selector()  # Select A Deck


if _input() is 1:  # Play AI Game
    print('AI Game Selected, waiting for Main Menu...')
    ai_game()

# NOTES
# Convolution 2D, use it
