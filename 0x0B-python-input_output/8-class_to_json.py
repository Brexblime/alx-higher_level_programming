#!/usr/bin/python3
"""returns the dictionary description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """Converts an object to a JSON-serializable dictionary."""
    json_dict = {}

    if hasattr(obj, '__dict__'):
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
    return (json_dict)
