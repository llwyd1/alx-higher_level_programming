#!/usr/bin/python3
"""Module containing a class that defines a square"""


class Square:
    """Defines a square
    Private instance attribute: size:
    - property def size(self)
    - property setter def size
    Instantiation with optional: size
    Public instance method: def area(self)
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0):
        """Initializes data"""
        self.__size = size

    @property
    def size(self):
        """Retrieves data"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
