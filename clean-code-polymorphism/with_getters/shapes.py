from precompute_constants.shapes import CIRCLE_CONSTANT
from utilities import ConstructorSet

class PropertiesSquare:
    def __init__(self, width: float):
        self.width = width
        self._area = width * width

    @property
    def area(self):
        return self._area


class PropertiesRectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = width * height

    @property
    def area(self):
        return self._area


class PropertiesTriangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = 0.5 * width * height

    @property
    def area(self):
        return self._area


class PropertiesCircle:
    def __init__(self, width: float):
        self.width = width
        self._area = CIRCLE_CONSTANT * width * width

    @property
    def area(self):
        return self._area


PROPERTIES_CONSTRUCTORS: ConstructorSet = {
    'square': PropertiesSquare,
    'rectangle': PropertiesRectangle,
    'triangle': PropertiesTriangle,
    'circle': PropertiesCircle
}


class GetterSquare:
    def __init__(self, width: float):
        self.width = width
        self._area = width * width

    def area(self):
        return self._area


class GetterRectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = width * height

    def area(self):
        return self._area


class GetterTriangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = 0.5 * width * height

    def area(self):
        return self._area


class GetterCircle:
    def __init__(self, width: float):
        self.width = width
        self._area = CIRCLE_CONSTANT * width * width

    def area(self):
        return self._area


GETTER_CONSTRUCTORS: ConstructorSet = {
    'square': GetterSquare,
    'rectangle': GetterRectangle,
    'triangle': GetterTriangle,
    'circle': GetterCircle
}