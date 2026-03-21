#!/usr/bin/python3

# print numbers from 0 to 98 in decimal and hexadecimal with one print
for i in range(99):
    print("{:d} = {:x}".format(i, i), end=", " if i != 98 else "") 
