import math

from control.shapes import ControlSquare, ControlRectangle, Shape
from no_division.shapes import NoDivisionTriangle
from utilities import ConstructorSet


CIRCLE_CONSTANT = math.pi * 0.5 * 0.5

class PrecomputedConstCircle(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return CIRCLE_CONSTANT * self.width * self.width


PRECOMPUTED_CONSTRUCTORS: ConstructorSet = {
    'square': ControlSquare,
    'rectangle': ControlRectangle,
    'triangle': NoDivisionTriangle,
    'circle': PrecomputedConstCircle
}
