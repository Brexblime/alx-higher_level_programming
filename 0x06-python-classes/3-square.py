#!/usr/bin/python3
"""create a class name."""


class Square:
    """naming it Square."""
    def __init__(self, size=0):
        """defining a private instance attribute called size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """defining a public instance method called area."""

        return (self.__size ** 2)
