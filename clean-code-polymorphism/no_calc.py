from shapes import (
    NoCalcSquare,
    NoCalcRectangle,
    NoCalcTriangle,
    NoCalcCircle,
)
from utilities import get_random_float, calculate_total_area_no_calc, PerfSpec, run_specs

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000
SPECS = [
    PerfSpec(
        'no calc square',
        [NoCalcSquare(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
    PerfSpec(
        'no calc rectangle',
        [
            NoCalcRectangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'no calc triangle',
        [
            NoCalcTriangle(get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ]
    ),
    PerfSpec(
        'no calc circle',
        [NoCalcCircle(get_random_float()) for _ in range(NUM_SHAPES)],
    ),
]

if __name__ == '__main__':
    run_specs(
        'no calc',
        NUM_SHAPES,
        NUM_RUNS,
        SPECS,
        calculate_total_area_no_calc
    )
