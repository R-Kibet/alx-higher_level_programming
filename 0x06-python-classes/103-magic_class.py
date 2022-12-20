#!/usr/bin/python3
""" a  Python class MagicClass that does exactly
the same as the following Python bytecode:"""

import math


class MagicClass:
    """ constructor"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """ area"""
    def area(self):
        return self.__radius ** 2 * math.pi

    """circumference"""
    def circumference(self):
        return 2 * math.pi * self.
