""" 
    Defines class Rectangle and tests it by creating two Rectangle objects
"""
class Rectangle:
    """ 
        One object of this class stores one rectangle's length and width
    """
    count = 0
    def __init__(self):
        """
           Sets both height and width to 0
        """
        self.height = 0
        self.width = 0
        Rectangle.count = Rectangle.count + 1

    def setData(self, height, width):
        """
            Sets the object's dimensions to height by width
        """        
        if height < 0 and width < 0:
            raise ValueError( "height and width are both negative")
        elif height < 0:
            self.width = width
            raise ValueError("height is negative")
        elif width < 0:
            self.height = height
            raise ValueError(" width is negative")
            
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __str__(self):
        """
            returns a sentence that tells the height and width of the object
        """
        return "height = %i, and width = %i" % (self.height, self.width)


"""
    Creates two Rectangles object and calls methods on them for testing purposes
"""
if __name__ == "__main__":
    r1 = Rectangle()
    print (r1) # automatically calls __str__(self) method and prints the returned value
    r1.setData(3,4)
    print(r1.area())
    print ("count = " + str(r1.count))

    print (r1)
    r2 = Rectangle()
    r2.setData(5,6)
    print(r2.area())
    print ("count = " + str(r2.count))
    print (r2)