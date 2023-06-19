#!/usr/bin/python3
"""
module contains the Square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes a Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size attribute."""
        return (self.width)

    @size.setter
    def size(self, value):
        """setter method for size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes."""
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        returns a string representation of the Square instance.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        """returns the dictionary representation of a Square."""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            })
