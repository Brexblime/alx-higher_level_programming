#!/usr/bin/python3
"""define class Rectangle."""


class Rectangle:
    """
    Class Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        getter method to retrieve the width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method to set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method to retrieve the height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter method to set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns Rectangle area.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns Rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return (rectangle_str.rstrip())
