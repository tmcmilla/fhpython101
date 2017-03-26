"""
        File rectangleDoc
        Defines class Rectangle and tests it by creating two Rectangle objects and calling methods on them.
"""


class Rectangle:
    """
        One object of this class stores one rectangle's length and width
    """
    def __init__(self):
        """
            Sets both height and width to 0
        """
        self.height = 0
        self.width = 0

    def setData(self, height, width):
        """
        Sets the object's dimensions to height by width
        :param height:
        :param width:
        :return:
        """
        self.height = height
        self.width = width

    def __str__(self):
        """
        Returns a sentence that tells the height and width of the object.
        :return:
        """
        return "height = %i, and width = %i" % (self.height, self.width)


"""
Creates two Rectangle objects and calls methods on them for testing purposes
"""
if __name__=="__main__":
    r1 = Rectangle()
    print(r1)  # automatcially calls __str__(self) method and prints the returned value
    r1.setData(3, 4)
    print(r1)
    r2 = Rectangle()
    r2.setData(5, 6)
    print(r2)
    print("Rectangle.__doc__=" + Rectangle.__doc__)
    print("Rectangle.__init__.__doc__=" + Rectangle.__init__.__doc__)
    print("Rectangle.setData.__doc__=" + Rectangle.setData.__doc__)
    print("Rectangle.__str__.__doc__=" + Rectangle.__str__.__doc__)