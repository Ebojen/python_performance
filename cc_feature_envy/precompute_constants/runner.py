from control.runner import calculate_total_area_control
from precompute_constants.shapes import PRECOMPUTED_CONSTRUCTORS
from utilities import TestRunner

run_precomputed_constants = TestRunner(
    'precomputed constants',
    PRECOMPUTED_CONSTRUCTORS,
    calculate_total_area_control
)
