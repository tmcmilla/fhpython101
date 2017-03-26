# In file hand.py contains Hand class

import random
import json
import week9.playingCard as playingCard


class Hand:
    """
        One object of class Hand represents one hand containing a list of cards
    """
    rankSelection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suitSelection = ['h', 'c', 's', 'd']

    def __init__(self, numCardsInHand):
        """
            Set the Hand's initial number of Cards
        """
        # add Try catch
        self.cards = []
        while (numCardsInHand > 0):
            Hand._createCard(self)
            numCardsInHand -= 1

    def bjValue(self):
        """
            return the Hand's black jack value
        """
        value = 0
        for card in self.cards:
            value += card.bjValue()
        return value

    def hitMe(self):
        """
            Adds a Card to the Hand
        """
        Hand._createCard(self)

    def __str__(self):
        """
            Returns a string representation of the Hand, list of Cards
        """
        output = ""
        for card in self.cards:
            output += card.__str__() + '\n'
        return output

    def _createCard(self):
        """
            creates an unique card and adds it to Hand
        """
        while True:
            suit = random.choice(Hand.suitSelection)
            rank = random.choice(Hand.rankSelection)
            card = playingCard.Card(rank, suit)
            if card not in self.cards:
                self.cards.append(card)
                break

    def getNumberOfCards(self):
        """
        return the number of Cards in Hand
        """
        return len(self.cards)

    def addCard(self, card):
        """
            Add Card to Hand
        """
        if type(card) == playingCard.Card and card not in self.cards:
            self.cards.append(card)


def main():
    """
     Hand test case including serialization and deserialization of hand object
    """
    blackJackHand = Hand(2)  # Create a Hand with 2 Cards
    print("Current Black Jack Value: %i" % blackJackHand.bjValue())  # Display current black Jack Value
    print(blackJackHand)  # Print Hand
    print("Hit Me")
    blackJackHand.hitMe()  # Add a Card
    print("Current Black Jack Value: %i" % blackJackHand.bjValue())  # Display current black Jack Value
    print(blackJackHand)  # Print Hand

    fileName = "output.out"
    store(blackJackHand, fileName)  # Store Hand to File
    blackJackHand = None
    print("Load Hand From File")
    blackJackHand = load(fileName)  # Load Hand from File
    print("Current Black Jack Value: %i" % blackJackHand.bjValue())  # Display current black Jack Value
    print(blackJackHand)  # Print Hand


def store(blackJackHand, fileName):
    """
      Stores Hand to File, 'fileName'
    """
    if type(blackJackHand) != Hand:
        return

    handle = open(fileName, 'w')  # Open File handle to Write
    output = json.dumps(blackJackHand, default=jdefault)  # Create serialize object to Json String
    handle.write(output)  # Write string to file, flush, close handle
    handle.flush()
    handle.close()


def load(fileName):
    """
      Create Hand from file, 'fileName'
    """
    handle = open(fileName, 'r')  # Create handle to File to read
    input = json.loads(handle.read())  # Read from file deserizalize json into dictionary
    blackJackHand = Hand(0)  # Create Hand with 0 cards
    for item in input['cards']:  # Loop over 'cards' value, which is a list of rank, suit parameters and create Cards
        rank, suit = item['rank'], item['suit']
        card = playingCard.Card(int(rank), suit)
        blackJackHand.addCard(card)  # Add Card to Hand
    return blackJackHand  # Return hand


def jdefault(o):
    """
        Method to serialize hand Object
    """
    if isinstance(o, set):
        return list(o)
    return o.__dict__


if __name__ == "__main__":
    main()

