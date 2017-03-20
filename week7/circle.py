import shape
import math
import unittest


class Circle(shape.Shape):
    def __init__(self):
        self.radius = 0

    def setRadius(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * math.pi
    def __str__(self):
        return "radius of the circle = %i" % (self.radius)


class CircleTests(unittest.TestCase):
    def test1(self):
        c = Circle()
        self.assertTrue(c.area() == 0)
        self.assertTrue(str(c) == "Radius of the circle = 0")

if __name__ == "__main__":
    circle = Circle()
    circle.setRadius(5)
    print(circle)




