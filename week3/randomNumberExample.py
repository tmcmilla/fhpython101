"""
generates a random number between 1 and 10, and asks the user to guess what it is
"""
import random # needed to use randint()
secretNumber = random.randint(1,10)
userGuess = int(input("Pick a number between 1 and 10: "))
while userGuess != secretNumber :
    if userGuess > secretNumber :
        print ('Your Guess: ' + str(userGuess) + ' is too high')
    else:
        print('Your Guess: ' + str(userGuess) + ' is too low')
    userGuess = int(input("Pick a number between 1 and 10: "))
print("you got it!")