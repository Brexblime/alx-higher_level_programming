#!/usr/bin/python3
for d in range(0, 10):
    for k in range(d + 1, 10):
        if d == 8 and k == 9:
            print("{}{}".format(d, k), end='\n')
        else:
            print("{}{}, ".format(d, k), end='')
