from abc import ABC, abstractmethod
from enum import Enum
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class NaiveSquare(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return self.width * self.width


class NaiveRectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class NaiveTriangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height / 2


class NaiveCircle(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return math.pi * self.width / 2 * self.width / 2


ShapeType = Enum('ShapeType', ['SQUARE', 'RECTANGLE', 'TRIANGLE', 'CIRCLE'])


class ShapeUnion:
    def __init__(self, shape_type: ShapeType, width: float, height: float=0.0):
        self.type = shape_type
        self.width = width
        self.height = height


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


CIRCLE_CONSTANT = math.pi * 0.5 * 0.5

class PrecomputedConstCircle(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return CIRCLE_CONSTANT * self.width * self.width


class SlotsSquare(Shape):
    __slots__ = ('width',)
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return self.width * self.width


class SlotsRectangle(Shape):
    __slots__ = ('width', 'height')
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class SlotsTriangle(Shape):
    __slots__ = ('width', 'height')
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return 0.5 * self.width * self.height


class SlotsCircle(Shape):
    __slots__ = ('width',)
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return CIRCLE_CONSTANT * self.width * self.width


class NoCalcSquare:
    __slots__ = ('width', 'area')

    def __init__(self, width: float):
        self.width = width
        self.area = width * width


class NoCalcRectangle:
    __slots__ = ('width', 'height', 'area')

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.area = width * height


class NoCalcTriangle:
    __slots__ = ('width', 'height', 'area')

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.area = 0.5 * width * height


class NoCalcCircle:
    __slots__ = ('width', 'area')

    def __init__(self, width: float):
        self.width = width
        self.area = CIRCLE_CONSTANT * width * width
