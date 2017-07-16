from manager import Manager
from employee import Employee

""" Tests the total ordering of class Employee and class Manager """
if __name__ == "__main__":
    m = Manager()
    m2 = Manager()
    e = Employee()
    e2 =  Employee("Mickie")
    list = [m, e, e2, m2]
    print ("here is the original list:\n" )
    listString = ""
    for person in list:
        listString = listString + str(person) + "\n"
    print (listString)
    
    list.sort()
    print ("\nhere is the sorted list: \n" )
    listString = ""
    for person in list:
        listString = listString + str(person) + "\n"
    print (listString)
