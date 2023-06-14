#!/usr/bin/python3
"""defining write_file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) 
    and returns the number of characters written
    """

    char_count = 0
    with open(filename, mode='w', encoding='utf-8') as file:
        char_count = file.write(text)
    return (char_count)

