#!/usr/bin/python3
"""Define a class Student."""


class Student:
    """Represent a class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {g: getattr(self, g) for g in attrs if hasattr(self, g)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for g, v in json.items():
            setattr(self, g, v)
