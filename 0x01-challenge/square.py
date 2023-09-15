#!/usr/bin/python3
"""
Square class
"""


class Square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """constructor method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permieter_of_my_square(self):
        """perimeter of my square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """str representation of instance"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permieter_of_my_square())
