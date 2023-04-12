#!/usr/bin/python3
"""Define a file-appending function."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "abc", encoding="utf-8") as f:
        return f.write(text)
