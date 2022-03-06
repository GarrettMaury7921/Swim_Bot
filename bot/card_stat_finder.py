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
    # because riot's a bum (at least when I tried to use json files :( )
    file1 = open(sys.path[0] + "/bot/card_assets/set1-en_us.txt", "r", encoding='utf-8')
    file2 = open(sys.path[0] + "/bot/card_assets/set2-en_us.txt", "r", encoding='utf-8')
    file3 = open(sys.path[0] + "/bot/card_assets/set3-en_us.txt", "r", encoding='utf-8')
    file4 = open(sys.path[0] + "/bot/card_assets/set4-en_us.txt", "r", encoding='utf-8')
    file5 = open(sys.path[0] + "/bot/card_assets/set5-en_us.txt", "r", encoding='utf-8')

    # Loop through all sets and check where my cards are from
    for code in my_cards_clean:
        index = 0

        for line in file1:
            index += 1

            if code in line:
                print(code + 'found at line ' + str(index))
