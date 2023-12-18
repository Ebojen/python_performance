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

procedural_set = [
    data.loc[5, 'avg_time'],
    data.loc[6, 'avg_time'],
    data.loc[7, 'avg_time'],
    data.loc[8, 'avg_time'],
    data.loc[9, 'avg_time'],
]

data['%_diff_proc'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, procedural_set),
    axis=1
)

no_division_set = [
    data.loc[15, 'avg_time'],
    data.loc[16, 'avg_time'],
    data.loc[17, 'avg_time'],
    data.loc[18, 'avg_time'],
    data.loc[19, 'avg_time'],
]

data['%_diff_no_div'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, no_division_set),
    axis=1
)

precomputed_consts_set = [
    data.loc[20, 'avg_time'],
    data.loc[21, 'avg_time'],
    data.loc[22, 'avg_time'],
    data.loc[23, 'avg_time'],
    data.loc[24, 'avg_time'],
]

data['%_diff_precom'] = data.apply(
    lambda x: calc_perc_diff_from_set(x, precomputed_consts_set),
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
