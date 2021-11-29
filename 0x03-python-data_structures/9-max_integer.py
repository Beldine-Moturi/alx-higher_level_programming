#!/usr/bin/python3
def max_integer(my_list=[]):
    """return largest integer in a list"""
    length = len(my_list)
    if my_list is None or length == 0:
        return None
    my_list.sort()
    return my_list[length - 1]
