import math


class Circle:
    r: float

    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        diameter: float = 2 * self.r
        return diameter * math.pi


circ: Circle = Circle(r=2.0)
print(circ.area())


class Rectangle:
    w: float
    h: float

    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


rect: Rectangle = Rectangle(w=4.0, h=5.5)
print(rect.area())
