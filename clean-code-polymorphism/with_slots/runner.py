from control.runner import calculate_total_area_control
from with_slots.shapes import SLOTS_CONSTRUCTORS
from utilities import (
    generate_specs,
    run_specs
)


NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


def run_with_slots():
    specs = generate_specs('with slots', SLOTS_CONSTRUCTORS, NUM_SHAPES)
    return run_specs(
        NUM_RUNS,
        specs,
        calculate_total_area_control
    )
