#!/usr/bin/python3
def print_last_digit(number):
    """
    prints last digit of a number
    return this last digit
    """
    if number < 0:
        num = number * -1
        last_dig = num % 10
    else:
        last_dig = number % 10
    print('{}'.format(last_dig), end="")
    return last_dig
