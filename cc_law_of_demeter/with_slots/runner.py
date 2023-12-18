from control.runner import calculate_total_area_control
from with_slots.shapes import SLOTS_CONSTRUCTORS
from utilities import TestRunner


NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000

run_with_slots = TestRunner(
    'with slots',
    SLOTS_CONSTRUCTORS,
    calculate_total_area_control
)
