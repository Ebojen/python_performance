from functools import cmp_to_key
from random import random, randint
from timeit import timeit
from pprint import pprint

from tabulate import tabulate

from control_lambda_handler import lambda_handler as control_handler
from no_duplicate_code_lambda_handler import lambda_handler as no_dup_handler
from cc_lambda_handler import lambda_handler as cc_handler

NUM_CUSTOMERS = 59
NUM_ALBUMS = 347
NUM_EVENTS = 100
NUM_TRIALS = 100


def make_customer_event():
    return {
        "resource": "/customers",
        "httpMethod": "GET",
        "pathParameters": {"customer_id": randint(1, NUM_CUSTOMERS)},
    }


def make_album_event():
    return {
        "resource": "/albums",
        "httpMethod": "GET",
        "pathParameters": {"album_id": randint(1, NUM_ALBUMS)},
    }


def run_events(events, handler):
    for event in events:
        handler(event, "")


def run_test(test_config):
    results = timeit("lambda: run_events(**test_config)", number=NUM_TRIALS)
    return {
        "test_name": test_config["test_name"],
        "handler": test_config["handler_name"],
        "avg_time": results / NUM_TRIALS
    }


def main():
    configurations = [
        {
            "test_name": "All Customers",
            "handler_name": "No Duplication",
            "handler": no_dup_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "All Albums",
            "handler_name": "No Duplication",
            "handler": no_dup_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Mixed Customers and Albums",
            "handler_name": "No Duplication",
            "handler": no_dup_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
        {
            "test_name": "All Customers",
            "handler_name": "Clean Code",
            "handler": cc_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "All Albums",
            "handler_name": "Clean Code",
            "handler": cc_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Mixed Customers and Albums",
            "handler_name": "Clean Code",
            "handler": cc_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
        {
            "test_name": "All Customers",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "All Albums",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Mixed Customers and Albums",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
    ]

    results = [run_test(config) for config in configurations]
    def sorter(result_a, result_b):
        if result_a["test_name"] < result_b["test_name"]:
            return -1
        if result_a["test_name"] > result_b["test_name"]:
            return 1
        if result_a["test_name"] == result_b["test_name"]:
            if result_a["avg_time"] < result_b["avg_time"]:
                return -1
            if result_a["avg_time"] > result_b["avg_time"]:
                return 1
            else:
                return 0

    results.sort(key=cmp_to_key(sorter))
    print(tabulate(results, headers="keys"))

if __name__ == "__main__":
    main()