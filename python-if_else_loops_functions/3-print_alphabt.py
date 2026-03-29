#!/usr/bin/python3
for letter in range(26):
    if chr(letter + 97) == 'e' or chr(letter + 97) == 'q':
        continue
    print("{}".format(chr(97 + letter)), end="")
