#!/usr/bin/python3
c = 122
while c >= 65:
    print('{:c}'.format(c), end='')
    if c == 65:
        break
    elif c in range(97, 123):
        c -= 32
    elif c in range(65, 91):
        c += 32
    c -= 1
