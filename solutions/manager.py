""" One object of class Manager represents one Manager, who is an Employee witha title and a bonus
"""
from employee import Employee

class Manager (Employee):
    """ gives initial values to the instance variables in the object """
    def __init__(self):
        Employee.__init__(self)
        self.title = "animation"
        self.bonus = 0

    """ Returns the string representation of the Manager object """
    def __str__(self):
        return Employee.__str__(self) + "bonus:" + str(self.bonus) + "\ntitle: " + self.title + "\n"


