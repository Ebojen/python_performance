from typing import Protocol

from control.runner import calculate_total_area_control
from with_getters.shapes import GETTER_CONSTRUCTORS, PROPERTIES_CONSTRUCTORS
from utilities import TestRunner


NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


class PropertiesShape(Protocol):
    def area(self) -> float:
        """Returns the area of the shape"""


def calculate_total_area_with_properties(squares: list[PropertiesShape]) -> float:
    accumulator = 0
    for square in squares:
        # The following line looks like we are accessing the internals of a class
        # but this is the nature of properties in python, remember that area is a method
        accumulator += square.area
    return accumulator

run_with_properties = TestRunner(
    'with properties',
    PROPERTIES_CONSTRUCTORS,
    calculate_total_area_with_properties
)

run_with_getters = TestRunner(
    'with getters',
    GETTER_CONSTRUCTORS,
    calculate_total_area_control
)
