from enum import auto, Enum
from functools import partial

from utilities import ConstructorSet
from precompute_constants.shapes import CIRCLE_CONSTANT

class ShapeType(Enum):
    SQUARE = auto()
    RECTANGLE = auto()
    TRIANGLE = auto()
    CIRCLE = auto()


SHAPE_CONSTANTS_TBL = {
    ShapeType.SQUARE: 1,
    ShapeType.RECTANGLE: 1,
    ShapeType.TRIANGLE: 0.5,
    ShapeType.CIRCLE: CIRCLE_CONSTANT
}


class ShapeUnion:
    def __init__(self, shape_type: ShapeType, width: float, height: float):
        self.type = shape_type
        self.width = width
        self.height = height


class PreCompShapeUnion:
    def __init__(self, shape_type: ShapeType, width: float, height: float):
        self.type = shape_type
        self.width = width
        self.height = height
        self.rectangular_area = width * height


PROCEDURAL_CONSTRUCTORS: ConstructorSet = {
    'square': partial(ShapeUnion, ShapeType.SQUARE),
    'rectangle': partial(ShapeUnion, ShapeType.RECTANGLE),
    'triangle': partial(ShapeUnion, ShapeType.TRIANGLE),
    'circle': partial(ShapeUnion, ShapeType.CIRCLE),
}

PROCEDURAL_PRECOMP_CONSTRUCTORS: ConstructorSet = {
    'square': partial(PreCompShapeUnion, ShapeType.SQUARE),
    'rectangle': partial(PreCompShapeUnion, ShapeType.RECTANGLE),
    'triangle': partial(PreCompShapeUnion, ShapeType.TRIANGLE),
    'circle': partial(PreCompShapeUnion, ShapeType.CIRCLE),
}
