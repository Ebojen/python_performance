from typing import Any


def control_flatten(data: Any, parent_key: str = "root") -> list[dict]:
    flattened = [{}]
    if isinstance(data, dict):
        for key, value in data.items():
            flattened_parent_key = f"{parent_key}_{key}"
            flattened_values = control_flatten(value, flattened_parent_key)
            new_rows = []
            for row in flattened:
                for flattened_row in flattened_values:
                    new_rows.append({**row, **flattened_row})
            flattened = new_rows
    elif isinstance(data, list):
        flattened_list = []
        for idx, value in enumerate(data):
            flattened_parent_key = f"{parent_key}_{idx}"
            flattened_list = flattened_list + control_flatten(
                value, flattened_parent_key
            )
        new_rows = []
        for row in flattened:
            for flattened_row in flattened_list:
                new_rows.append({**row, **flattened_row})
        flattened = new_rows
    else:
        # Assume data is a string, number, or bool at this point
        for row in flattened:
            row[parent_key] = data

    return flattened
