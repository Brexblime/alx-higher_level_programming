#!/usr/bin/python3
"""creating a class name."""


class Square:
    """naming it Square."""
    def __init__(self, size=0, position=(0, 0)):
        """initializing size and position."""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """property to retrieve."""
        return (self.__size)

    @size.setter
    def size(self, size=0):
        """property  setter."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """position property to retrieve."""
        return self.__position

    @position.setter
    def position(self, value):
        """position property  setter"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """defining a public instance method called area."""
        return (self.__size ** 2)
        """returns the current square area."""
    def my_print(self):
        """defining a public instance method called my_print."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
