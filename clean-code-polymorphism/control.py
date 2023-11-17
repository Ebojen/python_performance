from shapes import (
    NaiveSquare,
    NaiveRectangle,
    NaiveTriangle,
    NaiveCircle,
)
from utilities import get_random_float, calculate_total_area_poly, PerfSpec, run_specs

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000
SPECS = [
    PerfSpec(
        'naive square',
        [NaiveSquare(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
    PerfSpec(
        'naive rectangle',
        [
            NaiveRectangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'naive triangle',
        [
            NaiveTriangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'naive circle',
        [NaiveCircle(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
]

if __name__ == '__main__':
    run_specs(
        'clean code',
        NUM_SHAPES,
        NUM_RUNS,
        SPECS,
        calculate_total_area_poly
    )
