#!/usr/bin/python3
from sys import argv
length = len(argv)
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
