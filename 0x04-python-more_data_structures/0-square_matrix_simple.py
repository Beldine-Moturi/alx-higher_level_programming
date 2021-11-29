#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes square values of all integers of a matrix"""
    return [[num**2 for num in my_list] for my_list in matrix]
