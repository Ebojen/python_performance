from shapes import (
    NoDivisionTriangle,
    NoDivisionCircle
)
from utilities import get_random_float, calculate_total_area_poly, PerfSpec, run_specs

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000
SPECS = [
    PerfSpec(
        'no division triangle',
        [
            NoDivisionTriangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'no division circle',
        [NoDivisionCircle(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
]

if __name__ == '__main__':
    run_specs(
        'no division',
        NUM_SHAPES,
        NUM_RUNS,
        SPECS,
        calculate_total_area_poly
    )
