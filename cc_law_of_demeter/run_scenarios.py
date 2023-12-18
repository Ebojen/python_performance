import json
from pathlib import Path

from control.runner import run_control
from precompute_constants.runner import run_precomputed_constants
from with_getters.runner import run_with_getters, run_with_properties
from with_slots.runner import run_with_slots
from with_attrs.runner import run_with_attrs
from coreys_way.runner import run_coreys_way

def main(results_file: str):
    num_shapes = 1_000
    num_runs = 1_000_000
    tests = [
        run_control,
        run_precomputed_constants,
        run_with_getters,
        run_with_properties,
        run_with_slots,
        run_with_attrs,
        run_coreys_way,
    ]
    results = []
    for test in tests:
        results += test.generate_specs(num_shapes).run_test(num_runs)
    with open(results_file, 'w', encoding='utf-8') as results_file:
        results_file.write(json.dumps(results, indent=4))

if __name__ == '__main__':
    write_path = Path(__file__).parent / Path('results.json')
    main(write_path)
