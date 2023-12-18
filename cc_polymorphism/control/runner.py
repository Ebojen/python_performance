from utilities import TestRunner
from control.shapes import Shape, NAIVE_CONSTRUCTORS

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


def calculate_total_area_control(shapes: list[Shape]) -> float:
    accumulator = 0
    for shape in shapes:
        accumulator += shape.area()
    return accumulator

run_control = TestRunner('control', NAIVE_CONSTRUCTORS, calculate_total_area_control)


# def run_control():
#     specs = generate_specs('control', NAIVE_CONSTRUCTORS, NUM_SHAPES)
#     return run_specs(
#         NUM_RUNS,
#         specs,
#         calculate_total_area_control
#     )
