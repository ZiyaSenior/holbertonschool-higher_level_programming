#!/usr/bin/python3

# print lowercase ASCII alphabet except 'q' and 'e' in one line
for c in range(97, 123):
    if c not in (101, 113):  # 101='e', 113='q'
        print("{}".format(chr(c)), end="")
