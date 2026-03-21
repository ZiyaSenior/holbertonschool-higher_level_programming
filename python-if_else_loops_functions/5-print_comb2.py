#!/usr/bin/python3

# print numbers from 0 to 99, two digits, separated by ', '
for i in range(100):
    print("{:02d}".format(i), end=", " if i != 99 else "\n")
