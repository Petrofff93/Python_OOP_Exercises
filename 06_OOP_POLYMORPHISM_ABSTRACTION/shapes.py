from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return pi * (self.__radius * self.__radius)

    def calculate_perimeter(self):
        return (self.__radius * 2) * pi


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return (self.__height + self.__width) * 2


r = Rectangle(10, 20)
print(r.calculate_perimeter())
print(r.calculate_area())
