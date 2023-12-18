from math import pi
from utilities import TestRunner
from coreys_way.shapes import (
    ShapeType,
    ShapeUnion,
    SHAPE_CONSTANTS_TBL,
    PROCEDURAL_CONSTRUCTORS
)

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


def get_area_with_lookup(shapes: list[ShapeUnion]):
    accumulator = 0
    for shape in shapes:
        accumulator = SHAPE_CONSTANTS_TBL[shape.type] * shape.width * shape.height
    return accumulator


run_coreys_way = TestRunner(
    'corey\'s way',
    PROCEDURAL_CONSTRUCTORS,
    get_area_with_lookup,
    True
)
