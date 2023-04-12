#!/usr/bin/python3
""" a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as o:
        for line in o:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "m") as m:
        w.write(text)
