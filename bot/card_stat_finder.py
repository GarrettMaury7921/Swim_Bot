import sys
import json


def get_card_stats(all_cards):
    # File Variables
    set1 = sys.path[0] + "/bot/card_assets/set1-en_us.json"
    set2 = sys.path[0] + "/bot/card_assets/set2-en_us.json"
    set3 = sys.path[0] + "/bot/card_assets/set3-en_us.json"
    set4 = sys.path[0] + "/bot/card_assets/set4-en_us.json"
    set5 = sys.path[0] + "/bot/card_assets/set5-en_us.json"

    # Open the files needed to search through to find the stats for each card in your hand
    file1 = open(set1, "r")
    file2 = open(set2, "r")
    file3 = open(set3, "r")
    file4 = open(set4, "r")
    file5 = open(set5, "r")

    # Unpack the Card codes
    my_cards, enemy_cards, clean_codes = all_cards

    # get the clean codes of enemy cards and my cards
    enemy_cards_clean = []
    my_cards_clean = []
    for card in clean_codes:
        # Check if a card is an enemy card
        for i in enemy_cards:
            if card in i:
                enemy_cards_clean.append(card)
        # Check if a card is in my hand
        for i in my_cards:
            if card in i:
                my_cards_clean.append(card)

    # print(enemy_cards_clean)
    # print(my_cards_clean)

    # Use json to search for codes
