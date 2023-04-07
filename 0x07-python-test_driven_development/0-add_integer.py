#!/usr/bin/python3
"""This is an integer addition function."""


def add_integer(a, b=98):
    """Addition of interger a and b to be returned.

    Raises:
    TypeError: if a or b is a non-integer and a non-float.
    """
    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance (b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))

if __name__ = "__main__":
    import doctest
    doctest.testmod()
