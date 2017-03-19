
functionList = [lambda x: x + x, lambda x: x* x, lambda x: x **x]

print(functionList[1](10))

for index in range(3):
    print("functionList[%i](5)=%i" % (index, functionList[index](5)))

def alterString(param):
    if type(param) != str:
        return None
    i = len(param)

    return str.capitalize(param)

def repetitiveString(copies, param= '$'):
    if type(copies) != int:
        return param
    return param * copies

# Test Alter String
param = 'hello'
param = alterString(param)
print(param)

# Test repetitiveString
print(repetitiveString(5))
print(repetitiveString(10, '*'))

dict1 = {1:'1', 2:'2'}
dict1[1] = '3'