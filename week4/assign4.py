# Assignment 4
# File Name : assign4.py
# This module will translate an integer to words

"""
Function: appendResult
Concatenates two strings, 'current' and 'resultToAdd', with specified deliminator,  'deliminator'
Returns a single string
"""

def appendResult(current, resultToAdd, deliminator):
    # Verify that all inputs are strings, if not return empty string
    if not isinstance(current, str) \
        or not isinstance(resultToAdd, str) \
        or not isinstance(deliminator, str):
        return ""
    if current and not current.isspace():               # Remove extra white spaces
        current.strip()
    if resultToAdd and not resultToAdd.isspace():       # Check that result to append is not empty and not a white space
        if deliminator and current:
            current += deliminator
        current += resultToAdd
    return current

"""
Function: determineMultiplierRemainder
"""
def determineMultiplierRemainder(number, key):
    multiplier = 0
    remainder = number % key
    if (remainder < number):
        multiplier = (int)(number/key)
    return multiplier, remainder

"""
Function: numberToWord
Returns 'remainder' and spelled out integer, 'output', by converting the 'number' into words 'numberToWordLookup' dictionary
"""
def numberToWord(number, numberToWordLookup):
    # execute Initialize variabled
    output = ""
    result = None
    if not isinstance(number, int):
        return "number is not an integer"
    if not isinstance(numberToWordLookup, dict):
        return "numberToWordLookup is not an dictionary"
    if number <= 0:
        return "number must be greater than zero"
    keylist = sorted(numberToWordLookup.keys(), reverse=True)                       # Sort integer keys from high to low
    remainder = number                                                              # Initializer Remainder
    for key in keylist:                                                             # Loop over ordered integer
        multiplier, remainder = determineMultiplierRemainder(remainder, key)        # Determine multiplier and new remainder
        if multiplier >= 1:
            if numberToWordLookup[key]['multiplier']:
                multiplier, result = numberToWord(multiplier, numberToWordLookup)
                output = appendResult(output, result, " ")
            output = appendResult(output, numberToWordLookup[key]['name'], " ")
        if remainder < min(numberToWordLookup):
            break;
    return remainder, output







