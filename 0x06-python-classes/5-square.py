#!/usr/bin/python3
"""creating a class name."""


class Square:
    """naming it Square."""
    def __init__(self, size=0):
        """initializing size."""
        self.__size = size

    @property
    def size(self):
        """property to retrieve."""
        return (self.__size)

    @size.setter
    def size(self, size=0):
        """property to setter."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """defining a public instance method called area."""
        return (self.__size ** 2)
        """returns the current square area."""
    def my_print(self):
        """defining a public instance method called my_print."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
