phoneBook = {'mickey' : '213-333-2341', 'minnie' : '510-540-2390', 'goofy' : '818-399-2763'}
print (phoneBook['minnie']) # 510-540-2390
if 'donald' in phoneBook:
    print (phoneBook['donald'])
print(phoneBook.keys()) # dict_keys['mickey', 'minnie', 'goofy']

print(tuple(phoneBook.keys())) # ('mickey', 'minnie', 'goofy')
phoneBook['donald'] = '415-638-4433'
print(phoneBook) # 'mickey': '213-333-2341', 'minnie': '510-540-2390', 'goofy': '818-399-2763', 'donald' :'415-638-4433' }
print(sorted(phoneBook)) # ['donald', 'goofy', 'mickey', 'minnie']
for character in phoneBook:
    print(character + ' has phone number ' + phoneBook[character])
for character in sorted(phoneBook):
    print(character + ' has phone number ' + phoneBook[character])
answer = int(input("what is 12 times 12?"))
while answer != 12*12:
    print("please try again")
    answer = int(input("what is 12 times 12?"))