from math import pi
from utilities import TestRunner
from procedural.shapes import (
    ShapeType,
    ShapeUnion,
    PROCEDURAL_CONSTRUCTORS
)

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


def get_area_if_else(shape: ShapeUnion):
    if shape.type == ShapeType.SQUARE:
        return shape.width * shape.width
    if shape.type == ShapeType.RECTANGLE:
        return shape.width * shape.height
    if shape.type == ShapeType.TRIANGLE:
        return shape.width * shape.height / 2
    if shape.type == ShapeType.CIRCLE:
        return pi * shape.width / 2 * shape.width / 2


def get_area_match(shape: ShapeUnion):
    match shape.type:
        case ShapeType.SQUARE:
            return shape.width * shape.width
        case ShapeType.TRIANGLE:
            return shape.width * shape.height / 2
        case ShapeType.CIRCLE:
            return pi * shape.width / 2 * shape.width / 2
        case ShapeType.RECTANGLE:
            return shape.width * shape.height


def calculate_total_area_procedural(shapes: list[ShapeUnion]):
    accumulator = 0
    for shape in shapes:
        accumulator += get_area_if_else(shape)
    return accumulator


def calculate_total_area_match(shapes: list[ShapeUnion]):
    accumulator = 0
    for shape in shapes:
        accumulator += get_area_match(shape)
    return accumulator


run_procedural = TestRunner(
    'procedural',
    PROCEDURAL_CONSTRUCTORS,
    calculate_total_area_procedural
)

run_match = TestRunner(
    'procedural match',
    PROCEDURAL_CONSTRUCTORS,
    calculate_total_area_match
)
