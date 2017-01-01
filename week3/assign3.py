# Assignment 3
# File name : assign3.py
# This module will merge Dictionaries

"""
Function: dictionaryMerge
Returns a single dictionary, 'final', by merging a list of dictionaries, 'listToMerge'
In the case of duplicate keys, the corresponding value will be a List containing the original values
"""
def dictionaryMerge(listToMerge):
    final = {}                                              # Create an Empty Dictionary
    if not listToMerge:                                     # Check for whether supplied Parameter is NULL, return empty dictionary
        return final
    for dictItem in listToMerge:                            # Loop over Items
        if not isinstance(dictItem, dict):                  # Check for dictionary
            continue                                            # Not a dictionary, get next item
        for key, value in dictItem.items():                 # Get key, value pair, check for duplicate
            if key in final:
                final[key] = createList(final[key], value)  # Create a single List
            else:                                           # Key is unique, add Key/Value pair
                final[key] = value
    return final                                            # return merged dictionary

"""
Function: createList
Returns a single list, 'finalList', by merging the parameters, 'param1' and 'param2', into a single list
In the case if either parameters is a list, all items will be merged to create a single list
"""
def createList(param1, param2):
    finalList = []
    if not isinstance(param1, list):                # If param1 is not a list just append
        finalList.append(param1)
    else:                                           # If param1 is a list; loop through values
        for p in param1:
            finalList.append(p)
    if not isinstance(param2, list):                # If param2 is not a list just append
        finalList.append(param2)
    else:
        for p in param2:                            # If param2 is a list; loop through values
            finalList.append(p)

    return finalList                                # return List

# Start of Main Program
listToTest = []                                     # Create empty list

# Test Case 1 : Unique Keys
print("Test Case 1 : Unique Keys")

testDict1 = {'CA' : '1', 'NY' : '2', 'IL' : '3'}
testDict2 = {'OH' : '4', 'FL' : '5', 'TX' : '6'}
testDict3 = {'NJ' : '7', 'PA' : '8', 'MD' : '9'}
print("Test Dictionary 1: ", testDict1)
print("Test Dictionary 2: ", testDict2)
print("Test Dictionary 3: ", testDict3)

# Append Dictionaries to 'listToTest'
listToTest.append(testDict1)
listToTest.append(testDict2)
listToTest.append(testDict3)

# Merge Test Dictionaries
final = dictionaryMerge(listToTest)

# Print Merge Dictionary
print("Dictionaries Combined: ", final, '\n')

listToTest.clear()              # Clear List

#Test Case 2: Duplicate Keys and Triplicate Keys
print("Test Case 2 : Duplicate Keys and Triplicate Keys")

testDict1 = {'CA' : '1', 'NY' : '2', 'IL' : '3', 'FL' : '4'}
testDict2 = {'CA' : '5', 'OH' : '6', 'TX' : '7'}
testDict3 = {'CA' : '8', 'NY' : '9', 'PA' : '10', 'MD' : '11'}
print("Test Dictionary 1: ", testDict1)
print("Test Dictionary 2: ", testDict2)
print("Test Dictionary 3: ", testDict3)

# Append Dictionaries to 'listToTest'
listToTest.append(testDict1)
listToTest.append(testDict2)
listToTest.append(testDict3)

# Merge Test Dictionaries
final = dictionaryMerge(listToTest)

# Print Merge Dictionary
print("Dictionaries Combined: ", final, '\n')

listToTest.clear() # Clear List

# Test Case 3 : Mismatch of Lists and Single Values
print("Test Case 3 : Mismatch of Lists and Single Values")

testDict1 = {'CA' : '1', 'NY' : '2', 'IL' : ['3', '4'], 'OH' : ['5', '6']}
testDict2 = {'CA' : '7', 'FL' : '8', 'OH': '9', 'TX' : '10'}
testDict3 = {'CA' : '11', 'NY' : '12', 'TX' : ['13', '14'], 'IL' : ['15', '16']}
#Append Dictionaries to 'listToTest'
listToTest.append(testDict1)
listToTest.append(testDict2)
listToTest.append(testDict3)
# Print Test Dictionaries
print("Test Dictionary 1: ", testDict1)
print("Test Dictionary 2: ", testDict2)
print("Test Dictionary 3: ", testDict3)
# Merge Test Dictionaries
final = dictionaryMerge(listToTest)
"""
Result Should Be as Follows:
{'CA' :['1', '7', '11'],
'NY' : ['2', '12'],
'IL' : ['3', '4', '15', '16'],
'OH' : ['5', '6', '9'],
'FL' : '8',
'TX' : ['10', '13', '14'] }
"""
# Print Merge Dictionary
print("Dictionaries Combined: " , final)