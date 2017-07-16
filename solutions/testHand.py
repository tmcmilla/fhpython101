""" Tests class Hand by creating two Hand objects and calling methods on them
"""
from hand import Hand

if __name__ == "__main__":

    handForPlayer1 = Hand(10)
    print (handForPlayer1 )
    print (handForPlayer1.bjValue())
    
    handForPlayer2 = Hand()
    print (handForPlayer2)
    handForPlayer2.hitMe()
    print (handForPlayer2)

 
