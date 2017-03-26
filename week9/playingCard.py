"""
    File : playingCard.py
    Defines class Card for a single playing card suit and rank value
"""


class Card:
    # rank Lookup containing name and corresponding black JackValue
    rankLookup = {1: {'name': 'Ace', 'value': 1}, 2: {'name': 'Two', 'value': 2}, 3: {'name': 'Three', 'value': 3},
                  4: {'name': 'Four', 'value': 4},
                  5: {'name': 'Five', 'value': 5}, 6: {'name': 'Six', 'value': 6}, 7: {'name': 'Seven', 'value': 7},
                  8: {'name': 'Eight', 'value': 8},
                  9: {'name': 'Nine', 'value': 9}, 10: {'name': 'Ten', 'value': 10}, 11: {'name': 'Jack', 'value': 10},
                  12: {'name': 'Queen', 'value': 10},
                  13: {'name': 'King', 'value': 10}}
    # Suit Lookup
    suitLookup = {'h': 'Hearts', 'd': 'Diamonds', 'c': 'Clubs', 's': 'Spades'}
    def __init__(self, rank, suit):
        """
            Verify that parameters rank and suit are the correct type and with range
            Initializes the object rank and suit values
        :param rank:
        :param suit:
        """
        if type(rank) != int:
            raise TypeError("{0} parameter argument {1} is NOT an Integer".format('rank', rank))
        if type(suit) != str:
            raise TypeError("{0} parameter argument {1} is Not a string".format('suit', suit))
        if rank not in Card.rankLookup:
            raise ValueError("{0} parameter argument {1} is NOT between 1 and 13".format('rank', rank))
        if suit not in Card.suitLookup:
            raise ValueError(
                "{0} parameter argument {1} is neither 'h' for Hearts, 'd' for Diamonds, 'c' for Clubs, nor 's' for Spades".format(
                    'suit', suit))
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """
            Returns rank value
        """
        return self.rank

    def getSuit(self):
        """
            Returns suit
        """
        return self.suit

    def bjValue(self):
        """
             Returns rank value with respect to the Black Jack Game
        """
        return Card.rankLookup[self.rank]['value']

    def __eq__(self, other):
        """
            Returns True if self == other, False otherwise
        """
        if type(other) != Card:
            return False
        return self.rank == other.rank and self.suit == self.suit

    def __str__(self):
        """
            Returns the Rank and Suit in spelled out
        """
        return str(Card.rankLookup[self.rank]['name']) + " of " + str(Card.suitLookup[self.suit])

if __name__=="__main__":
    # Rank and suit test cases
    testCaseLookup = {1: {'name': 'Invalid Rank Type', 'rank': 'q', 'suit': 'h'},
                      2: {'name': 'Rank out-of-Range', 'rank': 20, 'suit': 'h'},
                      3: {'name': 'Invalid Suit Type', 'rank': 7, 'suit': 5},
                      4: {'name': 'Invalid Suit', 'rank': 7, 'suit': 'q'},
                      5: {'name': 'Valid Test', 'rank': 7, 'suit': 'h'}}

    # Loop over test cases
    print("Test Playing Card\n")
    keys = testCaseLookup.keys()
    for key in keys:
        try:
            rank = testCaseLookup[key]['rank']
            suit = testCaseLookup[key]['suit']
            print("\nTest Case:{0}, rank={1}, suit={2}".format(testCaseLookup[key]['name'], rank, suit))
            playingCard = Card(rank, suit)
        except TypeError  as e:  # Catch TypeError
            print("TypeError: ", ", ".join(repr(e) for e in e.args))
        except ValueError as e:  # Catch  ValueError
            print("ValueError: ", ", ".join(repr(e) for e in e.args))
        else:  # Exceute if no TypeError or ValueError is thrown
            print("Method getRank: " + str(playingCard.getRank()))  # Print Rank
            print("Method getSuit: " + str(playingCard.getSuit()))  # Print Suit
            print("Method bjValue: ", str(playingCard.bjValue()))   # Print Black Jack Value
            print("Name Of Card: ", playingCard)                    # Print Name of Card