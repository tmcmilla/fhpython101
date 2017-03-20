# Assignment 6
# File Name : Assign6.py
# Playing Card class Test module: Create Card Object, handles the exceptions, and exercises the Card methods

from playingCard import Card


def main():
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
            print("Method bjValue: ", str(playingCard.bjValue()))  # Print Black Jack Value
            print("Name Of Card: ", playingCard)  # Print Name of Card


if __name__ == "__main__":
    main()
