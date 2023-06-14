#!/usr/bin/python3
"""defining read file"""


def read_file(filename=""):
    """Reads a text file (utf8)."""

    with open(filename, encoding="utf-8") as f:
        file = f.read()
        print(file, end="")
