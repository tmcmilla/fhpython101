name = 'Elaine' # name is a string
print(name[5]) # e
print (len(name)) # 6
print(name[2:4]) # ai
print(name[-1]) # e
print(name[ : 3]) # Ela
print(name[:]) # Elaine
print(name[:-3]) # Ela
print(name[: -1]) # Elain
print(name + ' Haight') # Elain Haight
print('-' * 5) # -----

collegeInfo = ['Foothill', 13630, 'Los Altos Hills']
print(collegeInfo[0] + ' has ' + str(collegeInfo[1]) + ' students.')
# convert collegeInfo [1] to a string before concatenating

# you can modify an existing element in a list
print(collegeInfo)
collegeInfo.append('CA')
print(collegeInfo)
officeHours =('Mon 9:00', 'Tue 9:00', 'Wed 9:00', 'Thu 9:00')
print(len(officeHours))
officeHoursAsList = list(officeHours) * 2

officeHoursAsList.sort()
officeHoursAsList.append('Fri 9:00')
print(officeHoursAsList)
officeHoursAsTuple = tuple(officeHoursAsList) # convert back to tuple using the tuple() function

name = 'elaine'
print(name.capitalize())
print(name)
listOfLetters =['a', 'b', 'c']
listOfLetters.insert(2, 'c')
print(listOfLetters)

number = int(input("Please type a number "))
digitNames =('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
result =[]
while number >0:
    currentDigit = number % 10 # modules operator gives remainder after integer division
    # in the case it is the rightmost digit
    result.append( digitNames[currentDigit])
    number = number // 10
name = ""
for i in reversed(result):
    name = name + " " +i
print (name)

print ( 'my birthday is on %s / %s / %s' % ('11', '27', '1966'))
testTuple = (1,2,3,4)
print(testTuple)
testTuple2 = (5, 6, 7, 8)
print(testTuple + testTuple2)
testTuple3 = tuple('hello')
print(testTuple)


