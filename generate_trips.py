import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
project = Path(__file__).resolve().parent
raw = project / "raw"
raw.mkdir(exist_ok=True)

drivers = [
    {
        "driver_id": f"D{number:03}",
        "cohort": "New" if number <= 15 else "Established",
    }
    for number in range(1, 31)
]

trips = []

for number in range(1, 601):
    driver = random.choice(drivers)
    trip_date = date(2026, 1, 1) + timedelta(days=random.randrange(59))
    app_version = "1.0" if trip_date.month == 1 else "1.1"
    total_miles = round(random.uniform(2, 55), 2)

    # These assumed relationships are part of the synthetic dataset.
    average_detection = 80 if app_version == "1.0" else 90
    if driver["cohort"] == "New":
        average_detection -= 5

    detection_pct = round(
        max(0, min(100, random.gauss(average_detection, 8))), 1
    )
    payable_miles = round(total_miles * detection_pct / 100, 2)

    trips.append({
        "trip_id": f"T{number:04}",
        "driver_id": driver["driver_id"],
        "driver_cohort": driver["cohort"],
        "trip_date": trip_date.isoformat(),
        "app_version": app_version,
        "total_miles": total_miles,
        "payable_miles": payable_miles,
        "beacon_detection_pct": detection_pct,
    })

# Plant three issues to investigate during validation.
trips[9]["beacon_detection_pct"] = ""
trips[19]["payable_miles"] = round(trips[19]["total_miles"] + 5, 2)
trips.append(trips[29].copy())

output = raw / "trips.csv"

with output.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=list(trips[0]))
    writer.writeheader()
    writer.writerows(trips)

print(f"Created {output.name}: {len(trips)} rows")
print("Synthetic trips for 30 drivers across January and February 2026")