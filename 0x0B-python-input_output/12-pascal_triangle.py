#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """returns a list of lists of integers rep the Pascal’s triangle """

    t = []
    if n == 0:
        return t

    t.append([1])

    for i in range(1, n):
        prev = t[-1]
        nxt = [1]
        for i in range(len(prev) - 1):
            nxt.append(prev[i] + prev[i + 1])
        nxt += [1]
        t.append(nxt)

    return t
