from timeit import timeit
from typing import Callable

from shapes import (
    NaiveSquare,
    NaiveRectangle,
    NaiveTriangle,
    NaiveCircle,
    NoCalcSquare,
    NoCalcRectangle,
    NoCalcTriangle,
    NoCalcCircle
)
from utilities import get_random_float

def time_instantiation(num_instances: int, constructor: Callable, num_args: int):
    return timeit(
        lambda: constructor(*[get_random_float() for _ in range(num_args)]),
        number=num_instances
    ) / num_instances

if __name__ == '__main__':
    naive_square_times = time_instantiation(1_000_000, NaiveSquare, 1)
    print(f'Avg Naive square times in seconds were {naive_square_times:.10f}')

    no_calc_square_times = time_instantiation(1_000_000, NoCalcSquare, 1)
    print(f'Avg NoCalc square times in seconds were {no_calc_square_times:.10f}')

    naive_rectangle_times = time_instantiation(1_000_000, NaiveRectangle, 2)
    print(f'Avg Naive rectangle times in seconds were {naive_rectangle_times:.10f}')

    no_calc_rectangle_times = time_instantiation(1_000_000, NoCalcRectangle, 2)
    print(f'Avg NoCalc rectangle times in seconds were {no_calc_rectangle_times:.10f}')

    naive_triangle_times = time_instantiation(1_000_000, NaiveTriangle, 2)
    print(f'Avg Naive triangle times in seconds were {naive_triangle_times:.10f}')

    no_calc_triangle_times = time_instantiation(1_000_000, NoCalcTriangle, 2)
    print(f'Avg NoCalc triangle times in seconds were {no_calc_triangle_times:.10f}')

    naive_circle_times = time_instantiation(1_000_000, NaiveCircle, 1)
    print(f'Avg Naive circle times in seconds were {naive_circle_times:.10f}')

    no_calc_circle_times = time_instantiation(1_000_000, NoCalcCircle, 1)
    print(f'Avg NoCalc circle times in seconds were {no_calc_circle_times:.10f}')
