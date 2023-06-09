#!/usr/bin/python3
"""creating a class name."""


class BaseGeometry:
    """naming it BaseGeometry."""
    def area(self):
        """defining area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """defining Rectangle."""
    def __init__(self, width, height):
        """initialize Rectangle instance"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
