from utilities import TestRunner
from coreys_way.shapes import (
    ShapeUnion,
    PreCompShapeUnion,
    SHAPE_CONSTANTS_TBL,
    PROCEDURAL_CONSTRUCTORS,
    PROCEDURAL_PRECOMP_CONSTRUCTORS
)


def get_area_with_lookup(shapes: list[ShapeUnion]) -> float:
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


def get_area_with_lookup_precomp(shapes: list[PreCompShapeUnion]) -> float:
    accumulator = 0
    for shape in shapes:
        accumulator = SHAPE_CONSTANTS_TBL[shape.type] * shape.rectangular_area
    return accumulator


run_coreys_way_precomp = TestRunner(
    'corey\'s way precomp',
    PROCEDURAL_PRECOMP_CONSTRUCTORS,
    get_area_with_lookup_precomp,
    True
)
