#!/usr/bin/python3
""" class Square that defines a square by
Private instance attribute size
Private instance attribute: position"""


class Square:
    """ constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__positon = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.position[1] != 0:
                print("\n" * self.position[1], end='')
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)

    def __str__(self):
        to_print = ''
        if self.size != 0:
            if self.position[1] != 0:
                to_print += '\n' * self.position[1]
            for i in range(self.size):
                to_print += ' ' * self.position[0]
                to_print += '#' * self.size
                if i != self.__size - 1:
                    to_print += '\n'
        else:
            to_print = ''
        return to_print
