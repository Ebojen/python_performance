from pathlib import Path

import pandas as pd
from tabulate import tabulate, SEPARATING_LINE

from run_instantiation import main

main()

inst_data = pd.read_json('instantiation_results.json')

def calc_perc_diff_from_set(row: pd.Series, set: dict[str, float]) -> float:
    idx = int(row.name)
    comp_idx = idx % 4
    comp_avg = set[comp_idx]
    return (row['avg_time'] - comp_avg) / comp_avg * 100

control_set = [
    inst_data.loc[0, 'avg_time'],
    inst_data.loc[1, 'avg_time'],
    inst_data.loc[2, 'avg_time'],
    inst_data.loc[3, 'avg_time'],
]

inst_data['%_diff_control'] = inst_data.apply(
    lambda x: calc_perc_diff_from_set(x, control_set),
    axis=1
)

pretty_data = []
for idx, row in enumerate(inst_data.values.tolist()):
    pretty_data.append(row)
    if idx % 4 == 3 and idx != inst_data.shape[0] - 1:
        pretty_data.append(SEPARATING_LINE)

with open(
    Path(__file__).parent / Path('final_inst_results.txt'),
    'w', 
    encoding='utf-8'
) as file:
    file.write(tabulate(
        pretty_data,
        headers=inst_data.columns,
        tablefmt='rst',
        showindex=False,
        floatfmt=".8f"
    ))
