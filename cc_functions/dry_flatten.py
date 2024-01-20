from typing import Any


def make_new_key(parent: str, suffix: str) -> str:
    return f"{parent}_{suffix}"


def combine_rows(left: list[dict], right: list[dict]) -> list[dict]:
    new_rows = []
    for left_row in left:
        for right_row in right:
            new_rows.append({**left_row, **right_row})
    return new_rows


def dry_flatten(data: Any, parent_key: str = "root") -> list[dict]:
    flattened = [{}]
    if isinstance(data, dict):
        for key, value in data.items():
            flattened_parent_key = make_new_key(parent_key, key)
            flattened_values = dry_flatten(value, flattened_parent_key)
            flattened = combine_rows(flattened, flattened_values)
    elif isinstance(data, list):
        flattened_list = []
        for idx, value in enumerate(data):
            flattened_parent_key = make_new_key(parent_key, idx)
            flattened_list = flattened_list + dry_flatten(value, flattened_parent_key)
        flattened = combine_rows(flattened, flattened_list)
    else:
        # Assume data is a string, number, or bool at this point
        for row in flattened:
            row[parent_key] = data

    return flattened
