from enum import Enum
from functools import partial

from utilities import ConstructorSet


ShapeType = Enum('ShapeType', ['SQUARE', 'RECTANGLE', 'TRIANGLE', 'CIRCLE'])


class ShapeUnion:
    def __init__(self, shape_type: ShapeType, width: float, height: float=0.0):
        self.type = shape_type
        self.width = width
        self.height = height


PROCEDURAL_CONSTRUCTORS: ConstructorSet = {
    'square': partial(ShapeUnion, ShapeType.SQUARE),
    'rectangle': partial(ShapeUnion, ShapeType.RECTANGLE),
    'triangle': partial(ShapeUnion, ShapeType.TRIANGLE),
    'circle': partial(ShapeUnion, ShapeType.CIRCLE),
}
