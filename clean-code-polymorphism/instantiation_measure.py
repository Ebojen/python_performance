from timeit import timeit
from typing import Callable

from control.shapes import (
    ControlSquare,
    ControlRectangle,
    ControlTriangle,
    ControlCircle,
)
from with_getters.shapes import (
    GetterSquare,
    GetterRectangle,
    GetterTriangle,
    GetterCircle,
    PropertiesSquare,
    PropertiesRectangle,
    PropertiesTriangle,
    PropertiesCircle
)
from utilities import COLUMN_WIDTH, DIVIDER, HEADER, get_random_float

def time_instantiation(num_instances: int, constructor: Callable, num_args: int):
    return timeit(
        lambda: constructor(*[get_random_float() for _ in range(num_args)]),
        number=num_instances
    ) / num_instances

if __name__ == '__main__':
    num_runs = 1_000_000
    naive_square_times = f'{time_instantiation(num_runs, ControlSquare, 1)/num_runs:.20f}'
    getter_square_times = f'{time_instantiation(num_runs, GetterSquare, 1)/num_runs:.20f}'
    properties_square_times = f'{time_instantiation(num_runs, PropertiesSquare, 1)/num_runs:.20f}'

    naive_rectangle_times = f'{time_instantiation(num_runs, ControlRectangle, 2)/num_runs:.20f}'
    getter_rectangle_times = f'{time_instantiation(num_runs, GetterRectangle, 2)/num_runs:.20f}'
    properties_rectangle_times = f'{time_instantiation(num_runs, PropertiesRectangle, 2)/num_runs:.20f}'

    naive_triangle_times = f'{time_instantiation(num_runs, ControlTriangle, 2)/num_runs:.20f}'
    getter_triangle_times = f'{time_instantiation(num_runs, GetterTriangle, 2)/num_runs:.20f}'
    properties_triangle_times = f'{time_instantiation(num_runs, PropertiesTriangle, 2)/num_runs:.20f}'

    naive_circle_times = f'{time_instantiation(num_runs, ControlCircle, 1)/num_runs:.20f}'
    getter_circle_times = f'{time_instantiation(num_runs, GetterCircle, 1)/num_runs:.20f}'
    properties_circle_times = f'{time_instantiation(num_runs, PropertiesCircle, 1)/num_runs:.20f}'
    with open('instantiation_results.txt', 'w', encoding='utf-8') as results:
        results.write(HEADER)
        results.write(DIVIDER)
        results.write(
            f'|{"Control Square":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{naive_square_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Control Rectangle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{naive_rectangle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Control Triangle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{naive_triangle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Control Circle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{naive_circle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(DIVIDER)
        results.write(
            f'|{"Getter Square":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{getter_square_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Getter Rectangle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{getter_rectangle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Getter Triangle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{getter_triangle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Getter Circle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{getter_circle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(DIVIDER)
        results.write(
            f'|{"Properties Square":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{properties_square_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Properties Rectangle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{properties_rectangle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Properties Triangle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{properties_triangle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
        results.write(
            f'|{"Properties Circle":{" "}{">"}{COLUMN_WIDTH}}'
            f'|{properties_circle_times:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
