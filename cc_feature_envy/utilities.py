from random import choice, uniform
from timeit import timeit
from typing import Any, Callable, TypedDict


def get_random_float() -> float:
    """Used to generate a random float up to 2,147,483,647
    for creating instance of shapes of random dimensions.
    If you're unfamiliar with it, the underscore in a number
    in python is just a delimiter for readability much like a
    comma in common prose"""
    return uniform(0.1, 2_147_483_647)


class ConstructorSet(TypedDict):
    square: Callable
    rectangle: Callable
    triangle: Callable
    circle: Callable


class PerfSpec(TypedDict):
    name: str
    instances: list[Any]


class ResultSet(TypedDict):
    shape: str
    avg_time: float


class TestRunner:
    def __init__(
        self,
        test_name: str,
        constructor_set: ConstructorSet,
        objective_func: Callable[[list[Any]], float],
        is_coreys_way: bool = False
    ):
        self.test_name = test_name
        self.constructor_set = constructor_set
        self.objective_func = objective_func
        self.specs = []
        self.is_coreys_way = is_coreys_way

    def _generate_shape(self, shape_type, constructor):
        if shape_type in {'square', 'circle'}:
            if self.is_coreys_way:
                side_length = get_random_float()
                return constructor(side_length, side_length)
            return constructor(get_random_float())
        return constructor(get_random_float(), get_random_float())

    def _generate_random_shape(self) -> Any:
        name, constructor = choice(list(self.constructor_set.items()))
        return self._generate_shape(name, constructor)

    def generate_specs(self, num_shapes: int) -> 'TestRunner':
        for shape_type, constructor in self.constructor_set.items():
            self.specs.append({
                'name': f'{self.test_name} {shape_type}',
                'instances': [
                    self._generate_shape(shape_type, constructor)
                    for _ in range(num_shapes)
                ]
            })
        self.specs.append({
            'name': f'{self.test_name} assorted',
            'instances': [
                self._generate_random_shape()
                for _ in range(num_shapes)
            ]
        })
        return self

    def run_test(self, num_runs: int) -> list[ResultSet]:
        results: list[ResultSet] = []
        for spec in self.specs:
            avg_time = timeit(
                lambda: self.objective_func(spec['instances']),
                setup='gc.enable()',
                number=num_runs
            ) / num_runs
            results.append({
                'shape': spec['name'].title(),
                'avg_time': avg_time
            })
        return results
