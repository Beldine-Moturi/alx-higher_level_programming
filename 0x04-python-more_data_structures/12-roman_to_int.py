#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    """convert roman numeral to an integer"""
    num = []
    string = "IVXLCDM"
    numbers = [1, 5, 10, 50, 100, 500, 1000]
    for char in roman_string:
        for i, c in enumerate(string):
            if char == c:
                num.append(numbers[i])
#    for x in range(len(num) - 2):
#       if (num[x] < num[x + 1]):
#            num[x] = num[x] * -1
#    n = reduce(lambda x, y: x+y, num)
#    return n
