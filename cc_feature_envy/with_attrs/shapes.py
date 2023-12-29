from typing import Protocol

from utilities import ConstructorSet
from precompute_constants.shapes import CIRCLE_CONSTANT


class AttrShape(Protocol):
    width: float
    area: float


class AttrSquare:
    __slots__ = ['width', 'area']
    def __init__(self, width: float):
        self.width = width
        self.area = width * width


class AttrRectangle:
    __slots__ = ['width', 'height', 'area']
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.area = width * height


class AttrTriangle:
    __slots__ = ['width', 'height', 'area']
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.area = 0.5 * width * height


class AttrCircle:
    __slots__ = ['width', 'area']
    def __init__(self, width: float):
        self.width = width
        self.area = CIRCLE_CONSTANT * width * width


ATTR_CONSTRUCTORS: ConstructorSet = {
    'square': AttrSquare,
    'rectangle': AttrRectangle,
    'triangle': AttrTriangle,
    'circle': AttrCircle
}