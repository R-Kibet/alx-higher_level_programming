#!/usr/bin/python3
""" a class Square that defines a square"""


class Square:
    """ class construcor"""
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
