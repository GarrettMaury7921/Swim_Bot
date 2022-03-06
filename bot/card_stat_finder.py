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

    # Search through the file for the lines for the stats for MY cards
    my_cards_file1 = search_file_for_cards(1, my_cards_clean, debug)
    print(my_cards_file1)


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

        if debug is True:
            print(code)

        # Search for the card in file1
        for line in file:
            index += 1

            if code in line:
                code_found = True
                # INDEX -16 = Beginning of stats
                # INDEX + 17 = End of stats

                if debug is True:
                    print(code + ' found at line ' + str(index) + ' in file ' + str(file_num) + '. Stats begin at ' +
                          str(begin_stats) + ', stats end at ' + str(end_stats))

                begin_stats = index - 16
                end_stats = index + 17

                # file_lines format: <file number> <begin line> <end line for stats for that card>
                card_stats = file_num, begin_stats, end_stats
                file_lines.append(card_stats)

            if code_found is True:
                # Close file
                file.close()
                break

    return file_lines


# Extract the data from the files where the codes were found
def extract_data_from_file():
    pass
