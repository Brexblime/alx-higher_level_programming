#!/usr/bin/python3
"""Module for Rectangle class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Calculates the area.

        Raises:
            Exception: If area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The rectangle description.
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initializes a Square instance."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return (f"[Rectangle] {self.__size}/{self.__size}")
