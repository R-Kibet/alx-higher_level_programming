#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    i = 0
    if not my_list:
        pass
    for i in my_list[::-1]:
        print("{:d}".format(i))