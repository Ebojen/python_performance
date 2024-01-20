from timeit import timeit

from generate_data import generate_customer
from control_flatten import control_flatten
from dry_flatten import dry_flatten
from one_thing_flatten import one_thing_flatten

ITERATIONS = 1_000_000
NUM_DATA_ITEMS = 1_000


def flatten_data(func, data):
    for item in data:
        func(item)


def main():
    data = [generate_customer() for _ in range(NUM_DATA_ITEMS)]
    avg_control_time = (
        timeit(lambda: flatten_data(control_flatten, data), number=ITERATIONS)
        / ITERATIONS
    )
    avg_dry_time = (
        timeit(lambda: flatten_data(dry_flatten, data), number=ITERATIONS) / ITERATIONS
    )
    avg_one_time = (
        timeit(lambda: flatten_data(one_thing_flatten, data), number=ITERATIONS)
        / ITERATIONS
    )

    print("Avg Control Time in Seconds:", avg_control_time)
    print("Avg Dry Time in Seconds:", avg_dry_time)
    print(
        "Avg Dry % Diff Avg Control",
        (avg_dry_time - avg_control_time) / avg_control_time * 100,
    )
    print("Avg One Thing Time in Seconds:", avg_one_time)
    print(
        "Avg One Thing % Diff Avg Control",
        (avg_one_time - avg_control_time) / avg_control_time * 100,
    )


if __name__ == "__main__":
    main()
