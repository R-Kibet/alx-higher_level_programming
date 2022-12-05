#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    p = len(my_list) - 1
    c = my_list[:]
    if idx < 0:
        return (c)
    elif idx > p:
        return (c)
    else:
        c[idx] = element
    return (c)
