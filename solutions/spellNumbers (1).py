"""
Defines and tests a function spellNumber() that will spell out numbers in English. 
"""
def spellNumber(number):
    """ Returns a string containing the spelling of a number between -999999999 and 999999999
    """
    if number < 0:
        result = "negative "
        number = - number
    else :
        result = ""

    millions = number // 1000000
    if millions > 0:
        result += spellThreeDigits(millions) + " million"
    leftOver = number % 1000000
    
    thousands = leftOver //1000
    if thousands >0:
        result += spellThreeDigits(thousands) + " thousand"
    leftOver = leftOver %1000

    result += spellThreeDigits(leftOver)
    return result

def spellThreeDigits (number):
    """ Returns a string containting the spelling of a positive three digit number. 
    """
    words = {0: "", 1: " one", 2: " two",3: " three", 4: " four", 5: " five", 6: " six", 7: " seven", \
             8: " eight", 9: " nine", 10: " ten", 11: " eleven", 12: " twelve", 13: " thirteen", \
             14: " fourteen", 15: " fifteen", 16: " sixteen", 17: " seventeen", 18: " eighteen", \
             19: " nineteen", 20:" twenty", 30: " thirty", 40: " forty", 50: " fifty", 60:" sixty",\
             70: " seventy", 80: " eighty", 90: " ninety"}

    result = ""
    if number >999:
        return result
    if number //100 != 0:
        result += words[number//100] + " hundred"
        number = number % 100
    if number >= 20:
        tens = number - number % 10
        result += words[tens]
        number = number % 10
    result += words [number]
    return result

if __name__ == "__main__":
    print (spellNumber (123456789) )  
    print (spellNumber (456678) )   
    print (spellNumber (66) )       
    print (spellNumber (-123456789) )
    print (spellNumber (-456678) )      
    print (spellNumber (-418) )      
    print (spellNumber (-13456678) )      
    
    
        
