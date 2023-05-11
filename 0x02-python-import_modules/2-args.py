#!/usr/bin/python3
from sys import argv
length = len(argv) - 1
if length == 0:
    print("{:d} arguments.".format(length))
elif length == 1:
    print("{:d} argument:".format(length))
    print("{:d}: {:s}".format(length, argv[length]))
else:
    print("{:d} arguments:".format(length))
    for i in range(1, length + 1):
        print("{:d}: {:s}:".format(i, argv[i]))
