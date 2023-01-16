#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):

    """ inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ area of rectengle """
        return self.width * self.height

    def display(self):
        """ prints out instances in # """
        print("\n" * self.y,  end="")
        print((" " * self.x + "#" * self.__width + '\n')
              * self.__height, end="")

    def __str__(self):
        """String representation of the rectangle class"""
        str_res = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)
        return str_res

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            lst = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of a rectangle"""
        dic = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                dic[key.split("__")[-1]] = value
            else:
                dic[key] = value
        return dic
