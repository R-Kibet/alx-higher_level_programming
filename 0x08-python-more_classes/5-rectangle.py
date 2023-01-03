#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width property """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height property """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Return string to print rectangle with # """
        if self.__width == 0 or self.__height == 0:
            return ''
        prnt = ''
        for i in range(self.__height):
            for j in range(self.__width):
                prnt += '#'
            if i != self.__height - 1:
                prnt += '\n'
        return prnt

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """ Deconstructor """
        print("Bye rectangle...")
