#!/usr/bin/python3
"""
defining the class.
"""
def inherits_from(obj, a_class):
    """
    Check if the object is an instance.
    """
    if type(obj) == a_class:
        return (False)
    return (isinstance(obj, a_class))
