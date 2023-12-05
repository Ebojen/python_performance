from typing import Protocol

from control.runner import calculate_total_area_control
from with_getters.shapes import GETTER_CONSTRUCTORS, PROPERTIES_CONSTRUCTORS
from utilities import (
    generate_specs,
    run_specs
)


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


def run_with_properties():
    specs = generate_specs('with properties', PROPERTIES_CONSTRUCTORS, NUM_SHAPES)
    return run_specs(
        NUM_RUNS,
        specs,
        calculate_total_area_with_properties
    )


def run_with_getters():
    specs = generate_specs('with getters', GETTER_CONSTRUCTORS, NUM_SHAPES)
    return run_specs(
        NUM_RUNS,
        specs,
        calculate_total_area_control
    )
