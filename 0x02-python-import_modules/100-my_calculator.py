#!/usr/bin/python3
if __name__ == "__main__":
    """simple calculator"""
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = "{} {} {} = ".format(sys.argv[1], sys.argv[2], sys.argv[3])
    if sys.argv[2] == '+':
        print(result, "{}".format(int(sys.argv[1]) + int(sys.argv[3])))
    elif sys.argv[2] == '-':
        print(result, "{}".format(int(sys.argv[1]) - int(sys.argv[3])))
    elif sys.argv[2] == '*':
        print(result, "{}".format(int(sys.argv[1]) * int(sys.argv[3])))
    elif sys.argv[2] == '/':
        print(result, "{}".format(int(sys.argv[1]) / int(sys.argv[3])))
