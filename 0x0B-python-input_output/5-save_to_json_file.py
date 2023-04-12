#!/usr/bin/python3
"""Module of a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """An object written to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
