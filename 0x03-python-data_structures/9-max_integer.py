#!/usr/bin/python3

def max_integer(my_list=[]):

    p = len(my_list)

    if p == 0:
        return ("None")
    mx = my_list[0]

    for i in my_list:
        if i > mx:
            mx = i
    return (mx)
