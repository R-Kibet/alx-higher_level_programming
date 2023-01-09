#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ class that implements an exception"""
    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Exception """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))
        else:
            return value
