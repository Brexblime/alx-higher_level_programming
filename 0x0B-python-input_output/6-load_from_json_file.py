#!/usr/bin/python3
"""creates an Object from a 'JSON file'"""


import json


def load_from_json_file(filename):
    """defining load_from_json_file"""
    with open(filename, 'r') as f:
        return (json.load(f))
