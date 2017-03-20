#in file contact.py
class Contact:
    """
    One object of class Contact represents one person's contact info.
    """
    def __init__(self, name, phone, email, streetAddress):
        self.name = name
        self.phone = phone
        self.email = email
        self.streetAddress = streetAddress

    def __str__(self):
        return "%s\n%s\n%s\n%s\n" % \
               (self.name, self.phone,self.email,self.streetAddress)

if __name__ == "__main__":
    friend1 = Contact("Mickey", "650-345-3333", "Mickey@disneyland.com", "disneyland, CA")
    print (friend1)