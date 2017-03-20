"""
   extractString returns the middle character of argument param
"""
def extractString(param):
#  Verify that param is a string and is not empty
    if type(param) != str:
        raise TypeError("param is not a string")
    length = len(param)
    if length == 0:
        raise TypeError("param string is an string empty")

    loc = int(length/2)
    if (length % 2 == 1):   # Determine whether param length is even or odd in length
        return param[loc:loc+1]
    else:
        return param[loc-1:loc+1]

def midterm(*args, **kwargs):
    print(kwargs)

param = 'Hello'

print(extractString(param))

someList = [("A",1), ("B",2), ("C",3), ("D",4)]
someList.sort()
print(someList[3])

stringTemplate = "The passcode is: %s %s %s"
passCode =  tuple("dog")
print (stringTemplate % passCode)

midterm('a','b',3,4,5, A='90-100', B='80-89', C='70-79', D='hope not', F='ugh')

#someOtherList = ["E", "F"] + someList
print(someList[:2])

