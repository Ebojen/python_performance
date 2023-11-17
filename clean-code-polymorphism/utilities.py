from dataclasses import dataclass
from math import pi
from random import uniform
from timeit import timeit
from typing import Any, Callable

from shapes import Shape, NoCalcSquare, ShapeType, ShapeUnion


def calculate_total_area_poly(shapes: list[Shape]) -> float:
    accumulator = 0
    for shape in shapes:
        accumulator += shape.area()
    return accumulator


def get_random_float() -> float:
    return uniform(0.1, 2_147_483_647)


def get_area_if_else(shape: ShapeUnion):
    if shape.type == ShapeType.SQUARE:
        return shape.width * shape.width
    if shape.type == ShapeType.RECTANGLE:
        return shape.width * shape.height
    if shape.type == ShapeType.TRIANGLE:
        return shape.width * shape.height / 2
    if shape.type == ShapeType.CIRCLE:
        return pi * shape.width / 2 * shape.width / 2


def calculate_total_area_no_poly(shapes: list[ShapeUnion]):
    accumulator = 0
    for shape in shapes:
        accumulator += get_area_if_else(shape)
    return accumulator


def calculate_total_area_no_calc(squares: list[NoCalcSquare]) -> float:
    accumulator = 0
    for square in squares:
        accumulator += square.area
    return accumulator


@dataclass
class PerfSpec:
    shape: str
    values: list[Any]


def run_specs(
    run_name: str,
    num_shapes: int,
    num_runs: int,
    specs: list[PerfSpec],
    objective_func: Callable[[list[Any]], float]
):
    print(f'{run_name.title()} Results')
    print(
        f'Testing with {num_shapes:,} instances per shape. '
        f'Averaging over {num_runs:,} iterations.'
    )
    for spec in specs:
        avg_time = timeit(lambda: objective_func(spec.values), setup='gc.enable()', number=num_runs) / num_runs
        print(f'{spec.shape.title()} time averaged: {avg_time:.10f} s.')
