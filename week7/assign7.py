# Assignment 7
# File Name : Assign7.py
# Employee and Manager (IS-AN Employee) instantiation test module: Create Employee/Manager Objects and excecises the Objects methods


from manager import Manager
from employee import Employee

"""
    Create object Employee, verify instance variables and return object Employee
"""


def createEmployee(name, ssn, salary):
    employee = Employee(name, ssn, salary)
    # verify
    if name != employee.name or \
                    ssn != employee.ssn or \
                    salary != employee.salary:
        raise ValueError("Failed to initialize Employee")
    return employee


"""
    Create object Manager, verify instance variables and return object Manager
"""


def createManager(name, ssn, salary, title, yearBonus):
    manager = Manager(name, ssn, salary, title, yearBonus)
    if name != manager.name or \
                    ssn != manager.ssn or \
                    salary != manager.salary or \
                    title != manager.title or \
                    yearBonus != manager.yearBonus:
        raise ValueError("Failed to initialize Manager")
    return manager


"""
    loadEmployees takes the supplied List of parameters and creates corresponding Objects (Employee or Manager)
    return a list of Employee and Manager Objects
"""


def loadEmployees(testList):
    # define an empty employee List
    employeeList = []

    for item in testList:
        itemToAdd = None
        if item['type'] == 'employee':
            try:
                itemToAdd = createEmployee(item['name'],
                                           item['SSN'],
                                           item['salary'])
            except ValueError:
                continue

        elif item['type'] == 'manager':
            try:
                itemToAdd = createManager(item['name'],
                                          item['SSN'],
                                          item['salary'],
                                          item['title'],
                                          item['yearBonus'])
            except ValueError:
                continue
        # Add Employee/Manager Object to List
        if itemToAdd != None:
            employeeList.append(itemToAdd)

    return employeeList


def main():
    # create a list of test employees and managers
    testList = [{'type': 'employee', 'name': 'Mickey', 'SSN': '100-12-3456', 'salary': 1500.00},
                {'type': 'manager', 'name': 'Walt', 'SSN': '100-00-0000', 'salary': 5000.00,
                 'title': 'Head Of Disneyland', 'yearBonus': 1000.00},
                {'type': 'employee', 'name': 'Pluto', 'SSN': '100-65-4321', 'salary': 1000.00},
                {'type': 'manager', 'name': 'Minnie', 'SSN': '999-99-999', 'salary': 10000.00,
                 'title': 'Head Of Mouse HouseHold', 'yearBonus': 15000.00}]

    # Define percentRaise (0.1 == 10%)
    percentRaise = 0.1

    # Create Employees and Managers Object using the Test data
    employeeList = loadEmployees(testList)

    # Loop over Employee and Manager Objects
    for employee in employeeList:
        if type(employee) == Manager:
            print("Manager:")
        else:
            print("Employee:")
            # Print Employee or Manager
        print(employee)
        # Give Raise to Employee or Manager
        employee.giveRaise(percentRaise)
        # Print New Salary
        print("With %.2f%% Raise, Salary: $%.2f\n" % (percentRaise * 100, employee.salary))


if __name__ == "__main__":
    main()







