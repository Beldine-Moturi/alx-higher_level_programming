#!/usr/python3
def uppercase(str):
    for char in str:
        if ord(char) + 32 in range(97, 123):
            print('{:c}'.format(ord(char) + 32))
        else:
            print('{:c}'.format(char))
