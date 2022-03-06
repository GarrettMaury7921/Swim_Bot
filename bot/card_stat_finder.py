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
                break

        # Check if a card is my card
        for i in my_cards:
            if card in i:
                my_cards_clean.append(card)
                break

    # print(enemy_cards_clean)
    # print(str(my_cards_clean) + '\n')

    # Search through the file for the lines for the stats for MY cards
    my_cards_file1 = search_file_for_cards(1, my_cards_clean, debug)
    my_cards_file2 = search_file_for_cards(2, my_cards_clean, debug)
    my_cards_file3 = search_file_for_cards(3, my_cards_clean, debug)
    my_cards_file4 = search_file_for_cards(4, my_cards_clean, debug)
    my_cards_file5 = search_file_for_cards(5, my_cards_clean, debug)

    # Search through the file for the lines for the stats for ENEMY cards
    enemy_cards_file1 = search_file_for_cards(1, enemy_cards_clean, debug)
    enemy_cards_file2 = search_file_for_cards(2, enemy_cards_clean, debug)
    enemy_cards_file3 = search_file_for_cards(3, enemy_cards_clean, debug)
    enemy_cards_file4 = search_file_for_cards(4, enemy_cards_clean, debug)
    enemy_cards_file5 = search_file_for_cards(5, enemy_cards_clean, debug)

    if debug is True:
        print('My cards found from set 1 ' + str(my_cards_file1))
        print('Found from set 2 ' + str(my_cards_file2))
        print('Found from set 3 ' + str(my_cards_file3))
        print('Found from set 4 ' + str(my_cards_file4))
        print('Found from set 5 ' + str(my_cards_file5) + '\n')

        print('Enemy cards found from set 1 ' + str(enemy_cards_file1))
        print('Found from set 2 ' + str(enemy_cards_file2))
        print('Found from set 3 ' + str(enemy_cards_file3))
        print('Found from set 4 ' + str(enemy_cards_file4))
        print('Found from set 5 ' + str(enemy_cards_file5) + '\n')


# Put a number in for the file
def search_file_for_cards(file_num, card_codes, debug):
    # Attributes
    file_lines = []

    # Loop through all sets and check where my cards are from
    for code in card_codes:

        # Open the files needed to search through to find the stats for each card in your hand, encoding
        # because riot's a bum (at least when I tried to use json files :( )
        if file_num == 1:
            file = open(sys.path[0] + "/bot/card_assets/set1-en_us.txt", "r", encoding='utf-8')
        elif file_num == 2:
            file = open(sys.path[0] + "/bot/card_assets/set2-en_us.txt", "r", encoding='utf-8')
        elif file_num == 3:
            file = open(sys.path[0] + "/bot/card_assets/set3-en_us.txt", "r", encoding='utf-8')
        elif file_num == 4:
            file = open(sys.path[0] + "/bot/card_assets/set4-en_us.txt", "r", encoding='utf-8')
        elif file_num == 5:
            file = open(sys.path[0] + "/bot/card_assets/set5-en_us.txt", "r", encoding='utf-8')

        # Attributes
        index = 0
        begin_stats = 0
        end_stats = 0
        code_found = False

        # Search for the card in file1
        for line in file:
            index += 1

            if code in line:
                code_found = True
                # INDEX -16 = Beginning of stats
                # INDEX + 17 = End of stats

                begin_stats = index - 16
                end_stats = index + 17

                if debug is True:
                    print(code + ' found at line ' + str(index) + ' in set ' + str(file_num) + '. Stats begin at ' +
                          str(begin_stats) + ', stats end at ' + str(end_stats))

            if code_found is True:
                # Close file
                file.close()

                # file_lines format: <file number> <begin line> <end line for stats for that card>
                card_stats = file_num, begin_stats, end_stats
                file_lines.append(card_stats)
                break

    return file_lines


# Extract the data from the files where the codes were found
def extract_data_from_file():
    pass
