import traceback
class Card (object):
    """ Stores one playing card """
    
    def __init__(self, rank=1, suit='s'):
        """ rank is the number of the card (e.g. 12 is a Queen)
        suit is first char of suit ('s', 'h', 'c', 'd') """
        if rank >13:
            raise ValueError("initial rank too high")
        self.setRank(rank)
        self.setSuit(suit)

    def setRank (self, r):
        """ sets the rank to r, after checking its validity """
        self.rank = r

    def setSuit(self, s):
        """ sets the suite to s, after checking its validity """
        self.suit = s   

    def bjValue(self):
        """ returns the value the card would have in blackjack"""
        if self.rank < 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        result = ""
        if self.rank == 1: result = "Ace"
        elif self.rank == 2: result = "Two"
        elif self.rank == 3: result = "Three"
        elif self.rank == 4: result = "Four"
        elif self.rank == 5: result = "Five"
        elif self.rank == 6: result = "Six"
        elif self.rank == 7: result = "Seven"
        elif self.rank == 8: result = "Eight"
        elif self.rank == 9: result = "Nine"
        elif self.rank == 10: result = "Ten"
        elif self.rank == 11: result = "Jack"
        elif self.rank == 12: result = "Queen"
        elif self.rank == 13: result = "King"
        else: result = "N/A"
        result = result + " of "

        if self.suit == "s": result = result + "Spades"
        elif self.suit == "h": result = result + "Hearts"
        elif self.suit == "c": result = result + "Clubs"
        elif self.suit == "d": result = result + "Diamonds"
        else: result = result + "N/A"

        return result
    
if __name__ == "__main__":
    c1 = Card()
    print (c1)
    print (c1.bjValue())
    try:
        c2 = Card(17, 'c')
    except ValueError as specificError:
        print("printing traceback now:" + str(specificError.args))
        #traceback.print_exc()
    #5print (c2.bjValue())
"""
    print (c2)
    print (c2.bjValue())
    c3 = Card (3, 'h')
    print (c3)
    print (c3.bjValue())
    c1.setRank(13)
    print(c1)
    print(c1.bjValue())
"""
