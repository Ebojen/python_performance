from pathlib import Path
import pandas as pd
from tabulate import tabulate, SEPARATING_LINE

df = pd.read_json("./cc_functions/results.json")


def calc_perc_diff_from_reference(row: pd.Series, reference: dict[str, float]) -> float:
    idx = int(row.name)
    comp_idx = idx % 3
    comp_avg = reference[comp_idx]
    return (row["avg_time"] - comp_avg) / comp_avg * 100


control_set = [
    df.loc[0, "avg_time"],
    df.loc[1, "avg_time"],
    df.loc[2, "avg_time"],
]

df["%_diff_control"] = df.apply(
    lambda x: calc_perc_diff_from_reference(x, control_set), axis=1
)

dry_set = [
    df.loc[3, "avg_time"],
    df.loc[4, "avg_time"],
    df.loc[5, "avg_time"],
]

df["%_diff_dry"] = df.apply(lambda x: calc_perc_diff_from_reference(x, dry_set), axis=1)

clean_set = [
    df.loc[6, "avg_time"],
    df.loc[7, "avg_time"],
    df.loc[8, "avg_time"],
]

df["%_diff_clean"] = df.apply(
    lambda x: calc_perc_diff_from_reference(x, clean_set), axis=1
)

pretty_data = []
for idx, row in enumerate(df.values.tolist()):
    pretty_data.append(row)
    if idx % 3 == 2 and idx != df.shape[0] - 1:
        pretty_data.append(SEPARATING_LINE)

with open(
    Path(__file__).parent / Path("final_result.txt"), "a", encoding="utf-8"
) as file:
    file.write(
        tabulate(
            pretty_data,
            headers=df.columns,
            tablefmt="rst",
            showindex=False,
            floatfmt=".10f",
        )
    )