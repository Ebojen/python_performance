from control.runner import calculate_total_area_control
from precompute_constants.shapes import PRECOMPUTED_CONSTRUCTORS
from utilities import (
    generate_specs,
    run_specs
)


NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000


def run_precomputed_constants():
    specs = generate_specs('precomputed constants', PRECOMPUTED_CONSTRUCTORS, NUM_SHAPES)
    return run_specs(
        NUM_RUNS,
        specs,
        calculate_total_area_control
    )
