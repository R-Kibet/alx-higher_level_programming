#!/usr/bin/python3
"""Python class MagicClass that form bytecode oject"""
import math


class MagicClass:
    """ class constructor"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """finding the  area"""
    def area(self):
        return self.__radius ** 2 * math.pi

    """calculation of the circumference"""
    def circumference(self):
        return 2 * math.pi * self.
