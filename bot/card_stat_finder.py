import sys


def get_card_stats(self):
    # File Variables
    set1 = sys.path[0] + "/bot/card_assets/set1-en_us.json"
    set2 = sys.path[0] + "/bot/card_assets/set2-en_us.json"
    set3 = sys.path[0] + "/bot/card_assets/set3-en_us.json"
    set4 = sys.path[0] + "/bot/card_assets/set4-en_us.json"
    set5 = sys.path[0] + "/bot/card_assets/set5-en_us.json"

    # Open the files needed to search through to find the stats for each card in your hand
    file1 = open(self.set1, "r")
    file2 = open(self.set2, "r")
    file3 = open(self.set3, "r")
    file4 = open(self.set4, "r")
    file5 = open(self.set5, "r")
