#!/usr/bin/python3
""" class MyList inheriting from list """


class MyList(list):
    """ inherits from list """
    def print_sorted(self):
        """ output sorted list """
        print(sorted(self))
