import json
import sys


def get_card_stats(all_cards):
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

    # Open the files needed to search through to find the stats for each card in your hand, encoding
    # because riot's a bum
    file1 = open(sys.path[0] + "/bot/card_assets/set1-en_us.json", "r", encoding='utf-8')
    file2 = open(sys.path[0] + "/bot/card_assets/set2-en_us.json", "r", encoding='utf-8')
    file3 = open(sys.path[0] + "/bot/card_assets/set3-en_us.json", "r", encoding='utf-8')
    file4 = open(sys.path[0] + "/bot/card_assets/set4-en_us.json", "r", encoding='utf-8')
    file5 = open(sys.path[0] + "/bot/card_assets/set5-en_us.json", "r", encoding='utf-8')

    # Search for the codes in the card dictionary
    set1 = json.load(file1)
    set2 = json.load(file2)
    set3 = json.load(file3)
    set4 = json.load(file4)
    set5 = json.load(file5)

