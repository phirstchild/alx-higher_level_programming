#!/usr/bin/python3
"""Defines  lockedclass."""


class LockedClass:
    """
    This is to prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
