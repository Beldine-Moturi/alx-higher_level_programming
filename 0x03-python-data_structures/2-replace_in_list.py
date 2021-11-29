#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace element at index idx"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
