#!/usr/bin/python3
""" Finds a peak  """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    x = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return x[mid]
    elif mid - 1 < 0:
        return x[mid] if x[mid] > x[mid + 1] else x[mid + 1]
    elif mid + 1 >= length:
        return x[mid] if x[mid] > x[mid - 1] else x[mid - 1]

    if x[mid - 1] < x[mid] > x[mid + 1]:
        return x[mid]

    if x[mid + 1] > x[mid - 1]:
        return find_peak(x[mid:])
    return find_peak(x[:mid])
