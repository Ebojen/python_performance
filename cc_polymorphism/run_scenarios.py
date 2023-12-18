import json
from pathlib import Path

from control.runner import run_control
from no_division.runner import run_no_division
from precompute_constants.runner import run_precomputed_constants, run_precomputed_class_attr
from procedural.runner import run_procedural, run_match


def main(results_file: str):
    num_shapes = 1_000
    num_runs = 1_000_000
    tests = [
        run_control,
        run_procedural,
        run_match,
        run_no_division,
        run_precomputed_constants,
        run_precomputed_class_attr,
    ]
    results = []
    for test in tests:
        results += test.generate_specs(num_shapes).run_test(num_runs)
    with open(results_file, 'w', encoding='utf-8') as results_file:
        results_file.write(json.dumps(results, indent=4))

if __name__ == '__main__':
    write_path = Path(__file__).parent / Path('results.json')
    main(write_path)
