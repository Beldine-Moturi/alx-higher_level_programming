#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """return if multiple of 2 in a list"""
    return [not(i % 2) for i in my_list]
