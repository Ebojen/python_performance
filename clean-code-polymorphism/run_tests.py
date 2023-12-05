from control.runner import run_control
from no_division.runner import run_no_division
from precompute_constants.runner import run_precomputed_constants
from procedural.runner import run_procedural
from with_properties.runner import run_with_getters, run_with_properties
from with_slots.runner import run_with_slots
from utilities import COLUMN_WIDTH, DIVIDER, HEADER


if __name__ == '__main__':
    tests = [
        run_control,
        run_procedural,
        run_no_division,
        run_precomputed_constants,
        run_with_properties,
        run_with_getters,
        run_with_slots,
    ]
    with open('results.txt', 'w', encoding='utf-8') as results:
        results.write(HEADER)
        for test in tests:
            results.write(DIVIDER)
            results.write(test())
