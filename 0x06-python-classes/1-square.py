#!/usr/bin/python3
"""Module with a class that defines a square"""


class Square:
    """Defines a square
    Private instance attribute: size.
    instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """initializes data."""
        self.__size = size
