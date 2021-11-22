#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_dig = number % 10
elif number < 0:
    last_dig = ((number * -1) % 10) * -1
output_mes = 'Last digit of {} is {}'.format(number, last_dig)
if last_dig > 5:
    print(output_mes, 'and is greater than 5')
elif last_dig == 0:
    print(output_mes, 'and is 0')
else:
    print(output_mes, 'and is less than 6 and not 0')
