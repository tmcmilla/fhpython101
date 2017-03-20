# In file employee.py contains Employee class
from functools import total_ordering


# @total_ordering
class Employee:
    """
    One object of class Employee represents one employee identity with added capability to raise their salary
    """

    def __init__(self, firstName, lastName, ssn, salary):
        """
            Set the Employee's first name, last name, social security number (ssn) and initial salary
        """
        self.firstName = firstName
        self.lastName = lastName
        self.ssn = ssn
        self.salary = salary

    def __str__(self):
        """
            Return Employee's name, social security number (ssn), current salary
        """
        return "name: %s %s\nSSN: %s\nSalary: $%.2f" % \
               (self.firstName, self.lastName, self.ssn, self.salary)

    def giveRaise(self, percentRaise):
        """
            Raises the Employee's salary by supplied percentRaise (type::float)
        """
        self.salary = self.salary * (1.0 + percentRaise)

    def __eq__(self, other):
        """
        Returns True if self == other, False otherwise
        """
        # have to handle case
        if type(other) != Employee:
            return False
        return self.lastName.lower() == other.lastName.lower() and self.firstName.lower() == other.firstName.lower()

    def __lt__(self, other):
        """
        Returns True if self < other, False otherwise
        """
        if type(other) != Employee:  # Check that Other is an Employee if not return False
            return False

        if self.lastName.lower() < other.lastName.lower():
            return True
        elif self.lastName.lower() > other.lastName.lower():
            return False

        # Last names must be equal, check first Name
        elif self.firstName.lower() < other.firstName.lower():
            return True
        else:  # Either they are either the same or self > other ==> return False
            return False







