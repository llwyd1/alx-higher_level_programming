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

    def __init__(self, size=0, position=(0, 0)):
        """Initializes data"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves data"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position to a value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
