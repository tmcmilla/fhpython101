# In File manager.py contains Manager class
from employee import Employee


class Manager(Employee):
    """
        One object of class Manager represents one Manager (IS-AN Employee) with title and year bonus
    """

    def __init__(self, firstName, lastName, ssn, salary, title, yearBonus):
        """
            Sets the Manager's first name, last name, social security number (ssn), initial salary,
            title and year bonus
        """
        # Run Employee __init__
        Employee.__init__(self, firstName, lastName, ssn, salary)
        self.title = title
        self.yearBonus = yearBonus

    def __str__(self):
        """
            Return Mangers's name, social security number (ssn), current salary, title, and year Bonus
        """
        # Employee __str__ () and append manager specific instance variables
        return Employee.__str__(self) + "\nTitle: %s\nYearBonus: $%.2f" % (self.title, self.yearBonus)
