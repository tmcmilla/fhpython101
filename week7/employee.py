# In file employee.py contains Employee class

class Employee:
    """
    One object of class Employee represents one employee identity with added capability to raise their salary
    """
    def __init__(self, name, ssn, salary):
        self.name = name
        self.ssn = ssn
        self.salary = salary

    def __str__(self):
         return "name: %s\nSSN: %s\nSalary: $%.2f" % \
               (self.name, self.ssn,self.salary)

    def giveRaise(self, percentRaise):
        # try catch for a double
        # could it be negative
        # expect in raise
        self.salary = self.salary * (1.0 + percentRaise)






