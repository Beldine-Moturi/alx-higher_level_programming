#!/usr/bin/python3
def fizzbuzz():
    """
    prints numbers 1 to 100
    prints fizz in place of multiples of 3,
    buzz in place of multiples of 5
    and fuzzbuzz in place of multiples of 3 and 5
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end= " ")
        elif i % 3 == 0:
            print("Fizz", end= " ")
        elif i % 5 == 0:
            print("Buzz", end= " ")
        else:
            print(i, end= " ")
