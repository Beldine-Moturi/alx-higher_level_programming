#!/usr/bin/python3
"""Defines a class MyList that inherits from List"""


class MyList(list):
    """Description for the class MyList"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        assuming all elements of the list are of type int"""
        my_list = self[:]
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i+1]:
                tmp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = tmp
        print(my_list)
