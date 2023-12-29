from pathlib import Path

import pandas as pd
from tabulate import tabulate, SEPARATING_LINE

from run_scenarios import main

INTERMEDIATE_FILE = Path(__file__).parent / Path('results.json')

main(INTERMEDIATE_FILE)

data = pd.read_json(INTERMEDIATE_FILE)

def calc_perc_diff_from_set(row: pd.Series, set: dict[str, float]) -> float:
    idx = int(row.name)
    comp_idx = idx % 5
    comp_avg = set[comp_idx]
    return (row['avg_time'] - comp_avg) / comp_avg * 100

control_set = [
    data.loc[0, 'avg_time'],
    data.loc[1, 'avg_time'],
    data.loc[2, 'avg_time'],
    data.loc[3, 'avg_time'],
    data.loc[4, 'avg_time'],
]

data['%_diff_control'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, control_set),
    axis=1
)

precomputed_consts_set = [
    data.loc[5, 'avg_time'],
    data.loc[6, 'avg_time'],
    data.loc[7, 'avg_time'],
    data.loc[8, 'avg_time'],
    data.loc[9, 'avg_time'],
]

data['%_diff_precom'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, precomputed_consts_set),
    axis=1
)

with_getters_set = [
    data.loc[10, 'avg_time'],
    data.loc[11, 'avg_time'],
    data.loc[12, 'avg_time'],
    data.loc[13, 'avg_time'],
    data.loc[14, 'avg_time'],
]

data['%_diff_getters'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, with_getters_set),
    axis=1
)

with_slots_set = [
    data.loc[20, 'avg_time'],
    data.loc[21, 'avg_time'],
    data.loc[22, 'avg_time'],
    data.loc[23, 'avg_time'],
    data.loc[24, 'avg_time'],
]

data['%_diff_slots'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, with_slots_set),
    axis=1
)

with_attrs_set = [
    data.loc[25, 'avg_time'],
    data.loc[26, 'avg_time'],
    data.loc[27, 'avg_time'],
    data.loc[28, 'avg_time'],
    data.loc[29, 'avg_time'],
]

data['%_diff_attrs'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, with_attrs_set),
    axis=1
)

with_coreys_way_set = [
    data.loc[30, 'avg_time'],
    data.loc[31, 'avg_time'],
    data.loc[32, 'avg_time'],
    data.loc[33, 'avg_time'],
    data.loc[34, 'avg_time'],
]

data['%_diff_corey'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, with_coreys_way_set),
    axis=1
)

pretty_data = []
for idx, row in enumerate(data.values.tolist()):
    pretty_data.append(row)
    if idx % 5 == 4 and idx != data.shape[0] - 1:
        pretty_data.append(SEPARATING_LINE)

with open(
    Path(__file__).parent / Path('final_results.txt'),
    'w',
    encoding='utf-8'
) as file:
    file.write(tabulate(
        pretty_data,
        headers=data.columns,
        tablefmt='rst',
        showindex=False,
        floatfmt=".8f"
    ))
