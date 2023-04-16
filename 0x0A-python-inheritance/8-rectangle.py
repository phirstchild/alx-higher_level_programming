#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherited from BaseGeometry """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "height", height)
        self.__height__ = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width__ = width
