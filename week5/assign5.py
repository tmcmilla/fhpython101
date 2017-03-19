# Assignment 5
# File Name : Assign5.py
# Playing Card class Test module: Create Card Objects and Exercise the Methods


from playingCard import Card


def main():
    # Rank and suit test list
    testRankList = [1, 5, 10, 13]
    testSuitList = ['h', 's', 'c', 'd']

    # Loop over rank and suit lists
    print("Test Playing Cards\n")
    for rank in sorted(testRankList):
        for suit in sorted(testSuitList):
            try:
                print("Create Card Object: Rank: " + str(rank) + " Suit: " + str(suit))
                playingCard = Card(rank, suit)
                print("Method getRank: " + str(playingCard.getRank()))
                print("Method getSuit: " + str(playingCard.getSuit()))
                print("Method bjValue: ", str(playingCard.bjValue()))
                print("Name Of Card: ", playingCard)

                print("\n")
            except (ValueError, TypeError) as e:
                print(e)


if __name__ == "__main__":
    main()
