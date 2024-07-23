import json
from random import random, randint
from timeit import timeit

from control_lambda_handler import lambda_handler as control_handler
from dry_lambda_handler import lambda_handler as no_dup_handler
from cc_lambda_handler import lambda_handler as cc_handler

NUM_CUSTOMERS = 59
NUM_ALBUMS = 347
NUM_EVENTS = 1_000_000
NUM_TRIALS = 10_000_000


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
        "avg_time": results / NUM_TRIALS / NUM_EVENTS
    }


def main():
    configurations = [
        {
            "test_name": "Warm Up",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Warm Up",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Warm Up",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
        {
            "test_name": "Only Customers",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Only Albums",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Customers and Albums",
            "handler_name": "Control",
            "handler": control_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
        {
            "test_name": "Only Customers",
            "handler_name": "DRY",
            "handler": no_dup_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Only Albums",
            "handler_name": "DRY",
            "handler": no_dup_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Customers and Albums",
            "handler_name": "DRY",
            "handler": no_dup_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
        {
            "test_name": "Only Customers",
            "handler_name": "Clean Code",
            "handler": cc_handler,
            "events": [make_customer_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Only Albums",
            "handler_name": "Clean Code",
            "handler": cc_handler,
            "events": [make_album_event() for _ in range(NUM_EVENTS)],
        },
        {
            "test_name": "Customers and Albums",
            "handler_name": "Clean Code",
            "handler": cc_handler,
            "events": [
                make_customer_event() if random() < 0.5 else make_album_event()
                for _ in range(NUM_EVENTS)
            ],
        },
    ]

    results = [run_test(config) for config in configurations]
    cleaned_results = [result for result in results if result["test_name"] != "Warm Up"]
    with open("./cc_functions/results.json", "+w", encoding="utf-8") as file:
        file.write(json.dumps(cleaned_results, indent=4))


if __name__ == "__main__":
    main()