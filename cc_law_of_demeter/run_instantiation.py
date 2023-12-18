import json
from timeit import timeit
from typing import Callable

from control.shapes import (
    ControlSquare,
    ControlRectangle,
    ControlTriangle,
    ControlCircle,
)
from utilities import get_random_float

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

def time_instantiation(num_instances: int, constructor: Callable, num_args: int):
    return timeit(
        lambda: constructor(*[get_random_float() for _ in range(num_args)]),
        number=num_instances
    ) / num_instances

def main():
    num_runs = 1_000_000
    results = [
        {
            'shape': 'Control Square',
            'avg_time': time_instantiation(num_runs, ControlSquare, 1)/num_runs,
        },
        {
            'shape': 'Control Rectangle',
            'avg_time': time_instantiation(num_runs, ControlRectangle, 2)/num_runs,
        },
        {
            'shape': 'Control Triangle',
            'avg_time': time_instantiation(num_runs, ControlTriangle, 2)/num_runs,
        },
        {
            'shape': 'Control Circle',
            'avg_time': time_instantiation(num_runs, ControlCircle, 1)/num_runs,
        },
        {
            'shape': 'Getter Square',
            'avg_time': time_instantiation(num_runs, GetterSquare, 1)/num_runs,
        },
        {
            'shape': 'Getter Rectangle',
            'avg_time': time_instantiation(num_runs, GetterRectangle, 2)/num_runs,
        },
        {
            'shape': 'Getter Triangle',
            'avg_time': time_instantiation(num_runs, GetterTriangle, 2)/num_runs,
        },
        {
            'shape': 'Getter Circle',
            'avg_time': time_instantiation(num_runs, GetterCircle, 1)/num_runs,
        },
        {
            'shape': 'Properties Square',
            'avg_time': time_instantiation(num_runs, PropertiesSquare, 1)/num_runs,
        },
        {
            'shape': 'Properties Rectangle',
            'avg_time': time_instantiation(num_runs, PropertiesRectangle, 2)/num_runs,
        },
        {
            'shape': 'Properties Triangle',
            'avg_time': time_instantiation(num_runs, PropertiesTriangle, 2)/num_runs,
        },
        {
            'shape': 'Properties Circle',
            'avg_time': time_instantiation(num_runs, PropertiesCircle, 1)/num_runs,
        },
    ]

    with open('instantiation_results.json', 'w', encoding='utf-8') as results_file:
        results_file.write(json.dumps(results))

if __name__ == '__main__':
    main()
