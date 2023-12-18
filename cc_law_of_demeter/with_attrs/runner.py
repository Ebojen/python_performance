from utilities import TestRunner
from with_attrs.shapes import ATTR_CONSTRUCTORS, AttrShape


def calculate_total_area_attr(shapes: list[AttrShape]) -> float:
    accumulator = 0
    for shape in shapes:
        accumulator += shape.area
    return accumulator


run_with_attrs = TestRunner(
    'with attributes',
    ATTR_CONSTRUCTORS,
    calculate_total_area_attr
)
