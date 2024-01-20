from typing import Any


def make_new_key(parent: str, suffix: str) -> str:
    return f"{parent}_{suffix}"


def combine_rows(left: list[dict], right: list[dict]) -> list[dict]:
    new_rows = []
    for left_row in left:
        for right_row in right:
            new_rows.append({**left_row, **right_row})
    return new_rows


def flatten_primitive(data_primitive, parent_key, existing_rows):
    for row in existing_rows:
        row[parent_key] = data_primitive
    return existing_rows


def flatten_dict(data_dict, parent_key, existing_rows):
    for key, value in data_dict.items():
        flattened_parent_key = make_new_key(parent_key, key)
        flattened_values = one_thing_flatten(value, flattened_parent_key)
        existing_rows = combine_rows(existing_rows, flattened_values)
    return existing_rows


def flatten_list(data_list, parent_key, existing_rows):
    flattened_list = []
    for idx, value in enumerate(data_list):
        flattened_parent_key = make_new_key(parent_key, idx)
        flattened_list = flattened_list + one_thing_flatten(value, flattened_parent_key)
    existing_rows = combine_rows(existing_rows, flattened_list)
    return existing_rows


def one_thing_flatten(data: Any, parent_key: str = "root") -> list[dict]:
    flattened = [{}]
    if isinstance(data, dict):
        flattened = flatten_dict(data, parent_key, flattened)
    elif isinstance(data, list):
        flattened = flatten_list(data, parent_key, flattened)
    else:
        # Assume data is a string, number, or bool at this point
        flattened = flatten_primitive(data, parent_key, flattened)

    return flattened
