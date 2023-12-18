from control.runner import calculate_total_area_control
from precompute_constants.shapes import PRECOMPUTED_CONSTRUCTORS, PRECOMPUTED_CLASS_ATTR_CONSTRUCTORS
from utilities import TestRunner

run_precomputed_constants = TestRunner(
    'precomputed constants',
    PRECOMPUTED_CONSTRUCTORS,
    calculate_total_area_control
)

run_precomputed_class_attr = TestRunner(
    'precomputed class attr',
    PRECOMPUTED_CLASS_ATTR_CONSTRUCTORS,
    calculate_total_area_control
)
