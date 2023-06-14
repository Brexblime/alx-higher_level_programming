#!/usr/bin/python3
""" Function that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ defining class_to_json"""
    
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return (res)
