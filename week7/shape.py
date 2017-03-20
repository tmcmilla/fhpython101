import abc

class Shape(metaclass=abc.ABCMeta):
    """
        Defines the abstract superclass Shape in order to define the subclasses Rectangle and Circle.
        Defines the abstract method area() to ensure that any subclass of Shape fully define an area() method.
    """
    @abc.abstractmethod
    def area(self):
        return



