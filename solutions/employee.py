""" One object of class Employee represents one
    employee's personal info
"""
from functools import total_ordering

@total_ordering
class Employee :
    """ Initializes the object with a name, ssn and salary """
    def __init__(self, name="minnie"):
        self.name = name
        self.ssn = "345-66-4432"
        self.salary = 100000

    """ returns the string representation of the data in the object """       
    def __str__(self):
        return self.name + "\nssn: " + self.ssn + "\n$"+str(self.salary)+"\n"

    """ raises the salary member by "percentRaise" """
    def giveRaise(self, percentRaise):
        self.salary = self.salary * (1+percentRaise)

    """ returns true if the object is less than other, false otherwise """
    def __lt__(self, other):
        if self.name<other.name:
            return True
        else:
            return False

    """ returns true if the object is equal to other, false otherwise """
    def __eq__(self,other):
        if self.name==other.name:
            return True
        else:
            return False


