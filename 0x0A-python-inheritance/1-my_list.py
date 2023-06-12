#!/usr/bin/python3
"""creating a class called MyList."""


class MyList(list):
    """a class inherits from list."""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)."""
        sorted_list = sorted(self)
        print(sorted_list)
