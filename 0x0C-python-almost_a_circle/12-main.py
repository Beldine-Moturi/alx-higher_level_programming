#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle


if __name__ == "__main__":
    r1 = Rectangle(4, 5, 1, 2, 12)
    print(r1)
    print()
    print(r1.__dict__)
