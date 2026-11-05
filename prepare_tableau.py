import csv
from decimal import Decimal
from pathlib import Path

project = Path(__file__).resolve().parent

with (project / "clean_trips.csv").open(
    encoding="utf-8", newline=""
) as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames
    trips = list(reader)

output = project / "tableau_trips.csv"
new_columns = ["unpaid_miles", "payable_share_pct", "beacon_reading_status"]

with output.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[*columns, *new_columns])
    writer.writeheader()

    for trip in trips:
        total = Decimal(trip["total_miles"])
        payable = Decimal(trip["payable_miles"])

        writer.writerow({
            **trip,
            "unpaid_miles": f"{total - payable:.2f}",
            "payable_share_pct": f"{payable / total * 100:.4f}",
            "beacon_reading_status": (
                "Missing" if not trip["beacon_detection_pct"].strip()
                else "Available"
            ),
        })

print(f"Created {output.name}: {len(trips)} trips")