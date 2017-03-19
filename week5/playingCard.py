"""
    File : playingCard.py
    Defines class Card for a single playing card suit and rank value
"""

class Card:
    # rank Lookup containing name and corresponding black jackValue
    rankLookup = {1: {'name': 'Ace', 'value': 1}, 2: {'name': 'Two', 'value': 2}, 3: {'name': 'Three', 'value': 3},
                  4: {'name': 'Four', 'value': 4},
                  5: {'name': 'Five', 'value': 5}, 6: {'name': 'Six', 'value': 6}, 7: {'name': 'Seven', 'value': 7},
                  8: {'name': 'Eight', 'value': 8},
                  9: {'name': 'Nine', 'value': 9}, 10: {'name': 'Ten', 'value': 10}, 11: {'name': 'Jack', 'value': 10},
                  12: {'name': 'Queen', 'value': 10},
                  13: {'name': 'King', 'value': 10}}