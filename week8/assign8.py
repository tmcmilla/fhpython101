# Assignment 8
# File Name : Assign8.py
# Employee and Manager (IS-AN Employee) instantiation test module: Create Employee/Manager Objects and excecises the Objects methods


from manager import Manager
from employee import Employee


def createEmployee(firstName, lastName, ssn, salary):
    """
        Create object Employee, verify instance variables and return object Employee
    """
    employee = Employee(firstName, lastName, ssn, salary)
    # verify
    if firstName != employee.firstName or \
                    lastName != employee.lastName or \
                    ssn != employee.ssn or \
                    salary != employee.salary:
        raise ValueError("Failed to initialize Employee")
    return employee


def createManager(firstName, lastName, ssn, salary, title, yearBonus):
    """
        Create object Manager, verify instance variables and return object Manager
    """
    manager = Manager(firstName, lastName, ssn, salary, title, yearBonus)
    if firstName != manager.firstName or \
                    lastName != manager.lastName or \
                    ssn != manager.ssn or \
                    salary != manager.salary or \
                    title != manager.title or \
                    yearBonus != manager.yearBonus:
        raise ValueError("Failed to initialize Manager")
    return manager


def loadEmployees(testList):
    """
        loadEmployees takes the supplied List of parameters and creates corresponding Objects (Employee or Manager)
        return a list of Employee and Manager Objects
    """
    # define an empty employee List
    employeeList = []

    for item in testList:
        itemToAdd = None
        if item['type'] == 'employee':
            try:
                itemToAdd = createEmployee(item['firstName'],
                                           item['lastName'],
                                           item['SSN'],
                                           item['salary'])
            except ValueError:
                continue

        elif item['type'] == 'manager':
            try:
                itemToAdd = createManager(item['firstName'],
                                          item['lastName'],
                                          item['SSN'],
                                          item['salary'],
                                          item['title'],
                                          item['yearBonus'])
            except ValueError:
                continue
        # Add Employee/Manager Object to List
        if itemToAdd != None:  # Note : this line will call Employee __eq__ to verify that it is not equal to None
            employeeList.append(itemToAdd)

    return employeeList


def main():
    """
        Test Employee and Manager
    """
    # create a list of test employees and managers
    testList = [
        {'type': 'employee', 'firstName': 'Mickey', 'lastName': 'Mouse', 'SSN': '100-12-3456', 'salary': 1500.00},
        {'type': 'manager', 'firstName': 'Walt', 'lastName': 'Disney', 'SSN': '100-00-0000', 'salary': 5000.00,
         'title': 'Head Of Disneyland', 'yearBonus': 1000.00},
        {'type': 'employee', 'firstName': 'Donald', 'lastName': 'Duck', 'SSN': '100-65-4321', 'salary': 1000.00},
        {'type': 'manager', 'firstName': 'Minnie', 'lastName': 'Mouse', 'SSN': '999-99-999', 'salary': 10000.00,
         'title': 'Head Of Mouse HouseHold', 'yearBonus': 15000.00},
        {'type': 'manager', 'firstName': 'Daisy', 'lastName': 'Duck', 'SSN': '100-65-4321', 'salary': 12000.00,
         'title': 'Head Of Duck HouseHold', 'yearBonus': 10000.00}]

    # Define percentRaise (0.1 == 10%)
    percentRaise = 0.1

    # Create Employees and Managers Object using the Test data
    employeeList = loadEmployees(testList)

    # Sort employee List, which will ustilize Employee's __lt__ and __eq__ methods
    employeeList.sort()

    # Loop over Employee and Manager Objects
    print("Employees and Manager should be sorted by last name, then first\n")
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

        # Employee docStrings
    print("\nEmployee docstring for each method")
    print("Employee.__doc__=" + Employee.__doc__)
    print("Employee.__init__.__doc__=" + Employee.__init__.__doc__)
    print("Employee.giveRaise.__doc__=" + Employee.giveRaise.__doc__)
    print("Employee.__str__.__doc__=" + Employee.__str__.__doc__)
    print("Employee.__eq__.__doc__=" + Employee.__eq__.__doc__)
    print("Employee.__lt__.__doc__=" + Employee.__lt__.__doc__)

    print("\nManger docstring for each method")
    print(
        "Since Manager inherits from Employee, several of the methods ('giveRaise', '__eq__' and '__lt__') and the corresponding docstring will originate from the Employee class\n")
    print("Manager.__doc__=" + Manager.__doc__)
    print("Manager.__init__.__doc__=" + Manager.__init__.__doc__)
    print("Manager.giveRaise.__doc__=" + Manager.giveRaise.__doc__)
    print("Manager.__str__.__doc__=" + Manager.__str__.__doc__)
    print("Manager.__eq__.__doc__=" + Manager.__eq__.__doc__)
    print("Manager.__lt__.__doc__=" + Manager.__lt__.__doc__)


if __name__ == "__main__":
    main()







