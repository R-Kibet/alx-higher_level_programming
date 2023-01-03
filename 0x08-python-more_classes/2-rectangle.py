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
            self.__height = height
            self.__width = width

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
        a = self.__width * self.__height
        return a

    def perimeter(self):
        """ Return perimeter """
        p = (self.__width * 2) + (self.__height * 2)
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return p
