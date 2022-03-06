import sys


def get_card_stats(all_cards, debug):
    # Unpack the Card codes
    my_cards, enemy_cards, clean_codes = all_cards

    # print(my_cards)
    # print(enemy_cards)
    # print(str(clean_codes) + '\n')

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

    # Loop through all sets and check where my cards are from
    for code in my_cards_clean:
        # Open the files needed to search through to find the stats for each card in your hand, encoding
        # because riot's a bum (at least when I tried to use json files :( )
        file1 = open(sys.path[0] + "/bot/card_assets/set1-en_us.txt", "r", encoding='utf-8')
        file2 = open(sys.path[0] + "/bot/card_assets/set2-en_us.txt", "r", encoding='utf-8')
        file3 = open(sys.path[0] + "/bot/card_assets/set3-en_us.txt", "r", encoding='utf-8')
        file4 = open(sys.path[0] + "/bot/card_assets/set4-en_us.txt", "r", encoding='utf-8')
        file5 = open(sys.path[0] + "/bot/card_assets/set5-en_us.txt", "r", encoding='utf-8')

        # Attributes
        index = 0
        begin_stats = 0
        end_stats = 0
        code_found = False
        print(code)

        # Search for the card in file1
        for line in file1:
            index += 1

            if code in line:
                code_found = True
                # INDEX -16 = Beginning of stats
                # INDEX + 17 = End of stats
                print(code + 'found at line ' + str(index))

                begin_stats = index - 16
                end_stats = index + 17

                # print('stats begin at ' + str(begin_stats))
                # print('stats end at ' + str(end_stats))

            if code_found is True:
                # Close file
                file1.close()
                break
