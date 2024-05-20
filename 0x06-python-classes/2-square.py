#!/usr/bin/python3
"""Module containing a class that defines a square"""


class Square:
    """Defines a square
    Private instance attribute: size
    instantiation with optional size
    """

    def __init__(self, size=0):
        """validates and initializesa data"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
