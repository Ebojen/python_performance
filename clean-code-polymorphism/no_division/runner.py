from control.runner import calculate_total_area_control
from no_division.shapes import NO_DIVISION_CONSTRUCTORS
from utilities import (
    generate_specs,
    run_specs
)


NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


def run_no_division():
    specs = generate_specs('no division', NO_DIVISION_CONSTRUCTORS, NUM_SHAPES)
    return run_specs(
        NUM_RUNS,
        specs,
        calculate_total_area_control
    )
