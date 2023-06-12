#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


class BaseGeometry:
    """Defines the BaseGeometry class."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Defines the Rectangle class."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Computes the area of the Rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Defines the Square class."""

    def __init__(self, size):
        """Initializes a Square instance."""
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the Square."""
        return super().__str__()

    def area(self):
        """Computes the area of the Square."""
        return super().area()
