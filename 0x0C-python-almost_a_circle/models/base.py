#!/usr/bin/python3
""" Module containing the Base class """


class Base:
    """ Base class for managing id attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instance of the Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
