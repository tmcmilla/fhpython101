import shape
class Rectangle(shape.Shape):
    def __init__(self):
        self.width = 0
        self.length = 0
    def setWidth(self, width):
        self.width = width
    def setLength(self, length):
        self.length = length
    def area(self):
        return self.length * self.width
    def __str__(self):
        return "length: %s, width: %s of a rectangle" % (str(self.width), str(self.length))



