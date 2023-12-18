
from abc import abstractmethod, ABC
import math

from utilities import ConstructorSet


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class ControlSquare(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return self.width * self.width


class ControlRectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class ControlTriangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height / 2


class ControlCircle(Shape):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return math.pi * self.width / 2 * self.width / 2


NAIVE_CONSTRUCTORS: ConstructorSet = {
    'square': ControlSquare,
    'rectangle': ControlRectangle,
    'triangle': ControlTriangle,
    'circle': ControlCircle
}
