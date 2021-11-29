#!/usr/bin/python3
def uniq_add(my_list=[]):
    """add together all unique items in my_list"""
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
