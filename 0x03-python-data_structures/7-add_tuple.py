#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    if a == 0:
        x = 0
        y = 0
    elif a == 1:
        x = tuple_a[0]
        y = 0
    else:
        x = tuple_a[0]
        y = tuple_a[1]

    if b == 0:
        m = 0
        n = 0
    elif b == 1:
        m = tuple_b[0]
        n = 0
    else:
        m = tuple_b[0]
        n = tuple_b[1]

    t = (x + m, y + n)
    return (t)
