from shapes import (
    ShapeType,
    ShapeUnion
)
from utilities import get_random_float, calculate_total_area_no_poly, PerfSpec, run_specs

NUM_SHAPES = 1_000
NUM_RUNS = 1_000_000

SPECS = [
    PerfSpec(
        'no poly square',
        [ShapeUnion(ShapeType.SQUARE, get_random_float()) for _ in range(NUM_SHAPES)],
    ),
    PerfSpec(
        'no poly rectangle',
        [
            ShapeUnion(ShapeType.RECTANGLE ,get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ],
    ),
    PerfSpec(
        'no poly triangle',
        [
            ShapeUnion(ShapeType.TRIANGLE ,get_random_float(), get_random_float())
            for _ in range(NUM_SHAPES)
        ],
    ),
    PerfSpec(
        'no poly circle',
        [ShapeUnion(ShapeType.CIRCLE, get_random_float()) for _ in range(NUM_SHAPES)],
    ),
]

if __name__ == '__main__':
    run_specs(
        'no polymorphism',
        NUM_SHAPES,
        NUM_RUNS,
        SPECS,
        calculate_total_area_no_poly
    )
