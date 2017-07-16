""" One object of class Hand represents one Hand of cards. The cards in the
    Hand are randomly selected, but a deck of cards has not been implemented
    yet and so there may be more than one copy of a specific card in a Hand.
"""

from random import randrange
from Card import Card

class Hand:
    """ Stores a hand of Card objects. If the caller sends in a parameter,
        it is taken to be the number of cards in the hand. """
    def __init__(self, numCardsInHand = 5):
         self.numCardsInHand = 0
         self.hand = [ ]
         for i in range(numCardsInHand):
             self.hitMe()

    """ returns the blackjack value for the whole hand """
    def bjValue(self):
        value = 0
        for card in self.hand:
            value = value + card.bjValue()
        return value

    """ returns a string containing all the cards in the hand """
    def __str__(self):
        result = ""
        for i in range (self.numCardsInHand):
            result = result + str(self.hand[i]) + "\n"
        return result

    """ adds one randomly generated card to the Hand. """
    def hitMe(self):
        self.numCardsInHand = self.numCardsInHand +1
        suits = ('s', 'h', 'c', 'd')
        rank = randrange(1, 14)
        suit = suits[randrange (0, 4)]
        oneCard = Card(rank, suit)
        self.hand = self.hand + [oneCard]
        

            
