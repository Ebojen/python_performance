import math

from control.shapes import ControlSquare, ControlRectangle, Shape
from utilities import ConstructorSet


class NoDivisionTriangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return 0.5 * self.width * self.height


class NoDivisionCircle(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return math.pi * 0.5 * self.width * 0.5 * self.width


NO_DIVISION_CONSTRUCTORS: ConstructorSet = {
    'square': ControlSquare,
    'rectangle': ControlRectangle,
    'triangle': NoDivisionTriangle,
    'circle': NoDivisionCircle
}
