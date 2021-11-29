#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list"""
    if len(my_list) == 0:
        print(my_list)
    else:
        for i in my_list:
            print(i)
