# in file contactList.py
import contact
class ContactList:
    """
    One object of class ContactList represents a list of Contact objects. It
    can function as an address book
    """
    def __init__(self):
        self.list = []

    def add(self, newContact):
        self.list.append(newContact)

    def find(self, name):
        for item in self.list:
            if item.name == name:
                return str(item)
    def __str__(self):
        returnedString = ""
        for contact in self.list:
            returnedString = returnedString + "\n" + str(contact)
        return returnedString

if __name__ == "__main__":
    myFriends = ContactList()
    friend1 = contact.Contact("Mickey", "650-345-3333", "Mickey@disneyland.com", "Disneyland, California")
    friend2 = contact.Contact("Minnie", "650-345-3344", "Minnie@disneyworld.com", "Disneyworld, Florida")
    friend3 = contact.Contact("Donald", "650-345-3333", "Donald@EuroDisney.com", "EuroDisney, France")
    myFriends.add(friend1)
    myFriends.add(friend2)
    myFriends.add(friend3)
    print (myFriends)
    nameItem =  myFriends.find("Mickey")
    print(nameItem)