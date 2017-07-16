"""
Prints 3 form letters to console
No input from keyboard
"""

# tuple = (addressee, candidate, sender)
letter1 = ("Elaine", "Clinton", "Laura")
letter2 = ("James", "Obama", "Aloe")
letter3 = ("Dean", "Melissa", "Mom")
list = [letter1, letter2, letter3]
contents = "Dear %s, \nI would like you to vote for %s\nbecause I that this candidate is best\nfor the state.\n\nSincerely,\n%s\n"
for letterDetails in list:
    print (contents % letterDetails)




