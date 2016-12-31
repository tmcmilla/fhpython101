# Assignment 2
# File Name : assign2.py
# This module will create form letters

# Form Letter
formletter = '''Dear %s,\n
I would like you to vote for %s,\n
because I think he is best for this state.\n\n
Sincerely,\n\n%s'''

# List of Tuples containing: Addressee, Candidate, and Sender
inputs = [('Sheldon', 'Barbara Boxer', 'Jon Snow'),
          ('Leonard', 'Jerry Brown', 'Tyrion Lannister'),
          ('Penny', 'Kamala Harris', 'Arya Stark')]

# Loop thru the Tuples to form the individual letters
for input in inputs:
    print(formletter % input)
    print('\n')