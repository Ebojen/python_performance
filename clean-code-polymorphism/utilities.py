from dataclasses import dataclass
from random import choice, uniform
from timeit import timeit
from typing import Any, Callable, TypedDict


COLUMN_WIDTH = 35


def get_random_float() -> float:
    """Used to generate a random float up to 2,147,483,647
    for creating instance of shapes of random dimensions.
    If you're unfamiliar with it, the underscore in a number
    in python is just a delimiter for readability much like a
    comma in common prose"""
    return uniform(0.1, 2_147_483_647)


# This is strictly a type to be used for generating shapes of random types
ConstructorSet = TypedDict('ConstructorSet', {
    'square': Callable,
    'rectangle': Callable,
    'triangle': Callable,
    'circle': Callable
})


def generate_random_shape(constructors: ConstructorSet) -> Any:
    name, constructor = choice(list(constructors.items()))
    if name in ['square', 'circle']:
        return constructor(get_random_float())
    return constructor(get_random_float(), get_random_float())


@dataclass
class PerfSpec:
    shape: str
    values: list[Any]


def generate_specs(
    prefix: str,
    constructor_set: ConstructorSet,
    num_shapes: int=1_000
) -> list[PerfSpec]:
    return [
        PerfSpec(
            f'{prefix} square',
            [constructor_set['square'](get_random_float()) for _ in range(num_shapes)]
        ),
        PerfSpec(
            f'{prefix} rectangle',
            [
                constructor_set['rectangle'](get_random_float(), get_random_float())
                for _ in range(num_shapes)
            ]
        ),
        PerfSpec(
            f'{prefix} triangle',
            [
                constructor_set['triangle'](get_random_float(), get_random_float())
                for _ in range(num_shapes)
            ]
        ),
        PerfSpec(
            f'{prefix} circle',
            [constructor_set['circle'](get_random_float()) for _ in range(num_shapes)]
        ),
        PerfSpec(
            f'{prefix} assorted',
            [generate_random_shape(constructor_set) for _ in range(num_shapes)]
        ),
    ]


HEADER = (
    f'|{"Shape":{" "}{"^"}{COLUMN_WIDTH}}'
    f'|{"Average Time(s)":{" "}{"^"}{COLUMN_WIDTH}}|\n'
)
DIVIDER = f'|{"-" * COLUMN_WIDTH}|{"-" * COLUMN_WIDTH}|\n'


def run_specs(
    num_runs: int,
    specs: list[PerfSpec],
    objective_func: Callable[[list[Any]], float]
):
    results = ''
    for spec in specs:
        run_time = timeit(
            lambda: objective_func(spec.values),
            setup='gc.enable()',
            number=num_runs
        )
        avg_time = f'{run_time / num_runs:.10f}'
        results += (
            f'|{spec.shape.title():{" "}{">"}{COLUMN_WIDTH}}'
            f'|{avg_time:{" "}{">"}{COLUMN_WIDTH}}|\n'
        )
    return results
