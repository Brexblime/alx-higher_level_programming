#!/usr/bin/python3
"""returns the dictionary description with simple data structure 
(list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """ defining class_to_json"""
    
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return (res)
