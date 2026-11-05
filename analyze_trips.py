import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
from statistics import median

project = Path(__file__).resolve().parent

with (project / "clean_trips.csv").open(
    encoding="utf-8", newline=""
) as file:
    trips = list(csv.DictReader(file))

groups = defaultdict(list)

for trip in trips:
    groups[(trip["app_version"], trip["driver_cohort"])].append(trip)

output = project / "cohort_summary.csv"

with output.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "app_version",
        "driver_cohort",
        "trip_count",
        "driver_count",
        "total_miles",
        "payable_miles",
        "payable_share_pct",
        "median_trip_miles",
        "missing_beacon_readings",
    ])

    for (version, cohort), group in sorted(groups.items()):
        total = sum(Decimal(trip["total_miles"]) for trip in group)
        payable = sum(Decimal(trip["payable_miles"]) for trip in group)
        share = payable / total * 100
        median_miles = median(
            Decimal(trip["total_miles"]) for trip in group
        )
        driver_count = len({trip["driver_id"] for trip in group})
        missing = sum(
            not trip["beacon_detection_pct"].strip() for trip in group
        )

        writer.writerow([
            version, cohort, len(group), driver_count,
            f"{total:.2f}", f"{payable:.2f}", f"{share:.2f}",
            f"{median_miles:.2f}", missing,
        ])

        print(
            f"Version {version} | {cohort} | {len(group)} trips | "
            f"{share:.2f}% payable miles"
        )

print(f"\nCreated {output.name}")