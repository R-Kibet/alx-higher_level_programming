#!usr/bin/python3
""" Class Rectangle """


class Rectangle:

    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and height
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width property """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height property """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Return area of rectangle """
        a = self.width * self.height
        return a

    def perimeter(self):
        """ Return perimeter """
        p = (self.width * 2) + (self.height * 2)
        if (self.width == 0 or self.height == 0):
            return 0
        else:
            return p
