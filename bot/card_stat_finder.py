import sys


def get_card_stats(all_cards, debug):
    # Unpack the Card codes
    my_cards, enemy_cards, clean_codes = all_cards

    # print(my_cards) - Note: These cards are in order as they are in your hand in game
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

    # Actually get the data from the file with MY cards
    my_cards_stats = []
    for stats in my_cards_file1:
        if not stats:
            break
        else:
            my_cards_stats.append(extract_data_from_file(stats))
    for stats in my_cards_file2:
        if not stats:
            break
        else:
            my_cards_stats.append(extract_data_from_file(stats))
    for stats in my_cards_file3:
        if not stats:
            break
        else:
            my_cards_stats.append(extract_data_from_file(stats))
    for stats in my_cards_file4:
        if not stats:
            break
        else:
            my_cards_stats.append(extract_data_from_file(stats))
    for stats in my_cards_file5:
        if not stats:
            break
        else:
            my_cards_stats.append(extract_data_from_file(stats))

    # Actually get the data from the file with ENEMY cards
    enemy_cards_stats = []
    for stats in enemy_cards_file1:
        if not stats:
            break
        else:
            enemy_cards_stats.append(extract_data_from_file(stats))
    for stats in enemy_cards_file2:
        if not stats:
            break
        else:
            enemy_cards_stats.append(extract_data_from_file(stats))
    for stats in enemy_cards_file3:
        if not stats:
            break
        else:
            enemy_cards_stats.append(extract_data_from_file(stats))
    for stats in enemy_cards_file4:
        if not stats:
            break
        else:
            enemy_cards_stats.append(extract_data_from_file(stats))
    for stats in enemy_cards_file5:
        if not stats:
            break
        else:
            enemy_cards_stats.append(extract_data_from_file(stats))

    if debug is True:
        print('Format: <file number> <begin line> <end line for stats for that card>')
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

        print('MY EXTRACTED CARD STATS ' + str(my_cards_stats))
        print('ENEMY EXTRACTED CARD STATS ' + str(enemy_cards_stats) + '\n')

    # Return the stats of my cards and the enemies cards
    all_stats = [my_cards_stats, enemy_cards_stats]
    return all_stats


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

        # Search for the card in the specified file
        for line in file:
            index += 1

            if code in line:
                code_found = True
                # INDEX -16 = Beginning of stats
                # INDEX + 17 = End of stats

                begin_stats = index - 16
                end_stats = index + 17

            if code_found is True:
                # Close file
                file.close()

                # file_lines format: <file number> <begin line> <end line for stats for that card>
                card_stats = file_num, begin_stats, end_stats
                file_lines.append(card_stats)
                break

    return file_lines


# Extract the data from the files where the codes were found
def extract_data_from_file(card_stats):
    # Unpack the stats
    file_num, begin_line, end_line = card_stats

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
    card_data = ''

    # Search for the card in the specified file
    for line in file:
        index += 1

        # If we have reached the beginning line
        if index >= begin_line:

            # Get rid of some unnecessary lines if we find any
            # description line
            # level up description line
            # flavor text line
            # and the Artist name line
            if 'description' in line or 'levelupDescription' in line or 'flavorText' in line or 'artistName' in line:
                continue

            else:
                # Add each line to the string
                card_data += line

            # If we have reached the ending line
            if index == end_line:
                # End the loop
                break

    # Close file
    file.close()

    # Cleanup the card_data
    card_data = card_data.replace('\n', '')
    # Get rid of all tabs and whitespace, then put it all together again
    card_data = ''.join(card_data.split())

    return card_data


