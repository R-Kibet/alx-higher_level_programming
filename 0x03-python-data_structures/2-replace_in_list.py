#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    p = len(my_list) - 1

    if idx < 0:
        return (my_list)
    elif (idx > p):
        return (my_list)
    else:
        my_list[idx] = element
    return (my_list)
