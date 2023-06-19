#!/usr/bin/python4
"""
This module contains the Rectangle class.
"""


from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class, inheriting from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        attrs = ["y", "x", "id", "width", "height"]
        return ({attr: getattr(self, attr) for attr in attrs})

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be > 0.")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle."""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute."""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
