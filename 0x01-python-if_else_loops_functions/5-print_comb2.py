#!/usr/bin/python3
for d in range(0, 100):
    if d == 99:
        print("{:02d}".format(d), end='\n')
    print("{:02d}".format(d), end=',')
