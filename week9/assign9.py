# Assignment 9
# File Name : Assign9.py
# Hand instantiation test module: Create Hand Objects and exercises the Object methods

import hand


# Create Hand
def createHand(numCardsInHand):
    """
        Create object Hand, verify instance variables and return object Hand
    """
    blackJackHand = hand.Hand(numCardsInHand)
    # Verify that the number of cards in hand are to the number specified
    if numCardsInHand != blackJackHand.getNumberOfCards():
        raise ValueError("Failed to initialize Hand")
    return blackJackHand


def main():
    """
        Hand test cases
    """
    holdbjValue = 17  # Value at which to Hold
    backJack = 21  # Value Defined as Black Jack
    testCase = 0  # Test Case
    for numberOfInitialCards in range(0, 3):  # Number of initial Cards
        testCase += 1
        print("Test %i: Number of Initial Cards = %i " % (testCase, numberOfInitialCards))
        blackJackHand = createHand(numberOfInitialCards)  # Create Hand with i number of cards
        print(blackJackHand)  # Display current Hand
        print("Current Black Jack Value: %i" % blackJackHand.bjValue())  # Display current black Jack Value

        while blackJackHand.bjValue() < holdbjValue:  # Determine if the hand needs a hit
            print("Hit Me")
            blackJackHand.hitMe()  # Request another card
            print(blackJackHand)  # Display current Hand
            print("Current Black Jack Value: %i\n" % blackJackHand.bjValue())  # Display current black Jack Value

        if (blackJackHand.bjValue() == backJack):  # Display Current state of Hand
            print("BLACK JACK\n")
        elif blackJackHand.bjValue() > backJack:
            print("BUSTED!\n")
        else:
            print("HOLDING!\n")


if __name__ == "__main__":
    main()