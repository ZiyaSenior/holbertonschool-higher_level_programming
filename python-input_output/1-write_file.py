#!/usr/bin/python3
"""Module that writes a string to a file and returns its length"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 file and returns number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
