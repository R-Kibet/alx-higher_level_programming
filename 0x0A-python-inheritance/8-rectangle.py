#!/usr/bin/python3
"""
class rectangle inheriting from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeomtry """

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator('width', width)
	self.integer_validator('height', height)
        self.__width = width
        self.__height = height
