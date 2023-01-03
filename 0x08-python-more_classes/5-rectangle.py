#!usr/bin/python3
""" Area and perimeter """


class Rectangle:

    """ main class defines a rectangle
        Args:
            height
            width
    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        a = self.__width * self.__height
        return a

    def perimeter(self):
        p = (self.__width * 2) + (self.__height * 2)
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return p

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
