#!/usr/bin/python3
"""Module containing a class that defines a square"""


class Square:
    """Defines a square
    private instance attribute: size.
    instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
