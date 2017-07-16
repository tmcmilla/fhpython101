"""
    This is the solution of a student from last quarter named Mark O'Grady.
    This program merges N dictionaries into a single dictionary. If a given
    key exists in more than one of the original dictionaries, that key appears
    once in the merged dictionary and is mapped to a list containing ALL values
    that correspond it from the original dictionaries.
"""

# original dictionaries
addressBook = {'mary':'123 Main St.', 'devon':'3429 Cypress Dr.', 'erin':'9231 Sycamore Pl.', 'paul':'1332 Columbine Dr.', 'john':'4547 Reyes Dr.'}
cityState = {'john':'Palo Alto, CA'}
county = {}
phoneBook = {'erin':'(408) 250-4501', 'eric':'(886) 792-3847', 'devon':'(409) 345-1919', 'mary':'(972) 345-2239', 'john':'(650) 982-8732'}
email = {'mary':'mary.meyer@yopmail.com', 'david':'davidm@yopmail.com', 'john':'jsmith@maildrop.cc'}

# merged dictionary
db = addressBook    # start with the first dictionary in the merged set

# populate database
for dict in (cityState, county, phoneBook, email):
    for key, value in dict.items ():
        if key not in db:                   # if key not in db, insert key/vakue into db.
            db [key] = value
        elif type(db[key]) is not list:     # if key exists and value not list, create list with existing value and new value.
            db [key] = ([db[key], value])
        else:                               # key exists and value is already a list, so append to the entry db.
            db [key].append(value)

if __name__ == "__main__":
    print ('==============================   TESTING SECTION  ==============================')

    print ('Display Orignal Dictionaries:\n')
    print ('addressBook = %s' % addressBook)
    print ('cityState = %s' % cityState)
    print ('county = %s' % county)
    print ('phoneBook = %s' % phoneBook)
    print ('email = %s' % email)


    print ('\n\n\nDisplay New Merged Dictionary (db): \n')
    print ('db = %s' % db)




