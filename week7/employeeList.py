
"""
"""

from employee import Employee

class EmployeeList():
    def __init__(self):
        self.list = [] # create list

    def add(self, newEmployee):
        # Check that newEmployee is an Employee
        if type(newEmployee) == Employee:
            self.list.append(newEmployee)
        else:
            raise TypeError("newEmployee is NOT an Employee type")
    def __str__(self):
        # append the list
        returnedString = ""
        for employee in self.list:
            returnedString = returnedString + "\n" + str(employee)
        return returnedString



