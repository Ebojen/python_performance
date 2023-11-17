import sys

from shapes import (
    NaiveSquare,
    NaiveRectangle,
    NaiveTriangle,
    NaiveCircle,
    SlotsSquare,
    SlotsRectangle,
    SlotsTriangle,
    SlotsCircle,
)
from utilities import get_random_float, calculate_total_area_poly, PerfSpec, run_specs

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000
SPECS = [
    PerfSpec(
        'slots square',
        [SlotsSquare(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
    PerfSpec(
        'slots rectangle',
        [
            SlotsRectangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'slots triangle',
        [
            SlotsTriangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'slots circle',
        [SlotsCircle(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
]

if __name__ == '__main__':
    run_specs(
        'using slots',
        NUM_SHAPES,
        NUM_RUNS,
        SPECS,
        calculate_total_area_poly
    )
