#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print matrix of integers"""
    for i in matrix:
        for x, j in enumerate(i):
            print('{:d}'.format(j), end='')
            if x != (len(i) - 1):
                print(' ', end='')
        print()
