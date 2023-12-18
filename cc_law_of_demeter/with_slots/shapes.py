from control.shapes import Shape
from precompute_constants.shapes import CIRCLE_CONSTANT
from utilities import ConstructorSet


class SlotsSquare(Shape):
    __slots__ = ('width', '_area')
    def __init__(self, width: float):
        self.width = width
        self._area = width * width

    def area(self):
        return self._area


class SlotsRectangle(Shape):
    __slots__ = ('width', 'height', '_area')
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = width * height

    def area(self):
        return self._area


class SlotsTriangle(Shape):
    __slots__ = ('width', 'height', '_area')
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = 0.5 * width * height

    def area(self):
        return self._area


class SlotsCircle(Shape):
    __slots__ = ('width', '_area')
    def __init__(self, width: float):
        self.width = width
        self._area = CIRCLE_CONSTANT * width * width

    def area(self):
        return self._area


SLOTS_CONSTRUCTORS: ConstructorSet = {
    'square': SlotsSquare,
    'rectangle': SlotsRectangle,
    'triangle': SlotsTriangle,
    'circle': SlotsCircle
}
