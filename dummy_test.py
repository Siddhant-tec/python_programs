from abc import ABCMeta, abstractmethod, ABC


class Shape(metaclass=ABCMeta):
    def __init_(self):
        print("I am in init")

    @abstractmethod
    def draw_shape(self):
        pass

    @abstractmethod
    def set_color(self):
        pass


class Circle(Shape, ABC):
    def draw_shape(self):
        print("Draw Circle")

    def set_color(self):
        print("Red")


c = Circle()
c.draw_shape()
c.set_color()
