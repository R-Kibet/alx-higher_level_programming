#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Private instance attirubute: position
    Public instance method: def area(self)
    Public instance method: def my_print(self)
"""


class Square:
    """ constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        a = self.__size ** 2
        return a

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    """True if self is equal than other"""
    def __eq__(self, other):
        return self.area() == other.area()

    """True if self is greater or equal than other"""
    def __ge__(self, other):
        return self.area() >= other.area()

    """True if self is greater than other"""
    def __gt__(self, other):
        return self.area() > other.area()

    """True if self is not equeal other"""
    def __ne__(self, other):
        return self.area() != other.area()
