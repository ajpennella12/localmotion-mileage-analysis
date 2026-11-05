import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

project = Path(__file__).resolve().parent

with (project / "cohort_summary.csv").open(
    encoding="utf-8", newline=""
) as file:
    rows = list(csv.DictReader(file))

versions = sorted({row["app_version"] for row in rows})
shares = {
    (row["app_version"], row["driver_cohort"]):
        float(row["payable_share_pct"])
    for row in rows
}

positions = list(range(len(versions)))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")

for cohort, offset, color in [
    ("New", -width / 2, "#7396B8"),
    ("Established", width / 2, "#193549"),
]:
    values = [shares[(version, cohort)] for version in versions]
    bars = ax.bar(
        [position + offset for position in positions],
        values,
        width,
        label=cohort,
        color=color,
    )
    ax.bar_label(bars, labels=[f"{value:.2f}%" for value in values], padding=4)

ax.set_xticks(positions, [f"Version {version}" for version in versions])
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
ax.set_ylabel("Payable miles / total miles")
ax.set_title("Payable-mile share by driver cohort")
ax.legend(loc="upper left", frameon=False)
ax.grid(axis="y", alpha=0.2)
ax.set_axisbelow(True)
fig.supxlabel("Synthetic data • Version and month change together", fontsize=9)

fig.savefig(project / "cohort_comparison.png", dpi=180)
print("Created cohort_comparison.png")