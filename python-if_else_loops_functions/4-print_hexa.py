#!/usr/bin/python3

# print numbers from 0 to 98 in decimal and hexadecimal
for i in range(99):
    if i != 98:
        print("{:d} = {:x}, ".format(i, i), end="")
    else:
        print("{:d} = {:x}".format(i, i), end="") 
