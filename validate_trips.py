import csv
from decimal import Decimal
from pathlib import Path

project = Path(__file__).resolve().parent

with (project / "raw" / "trips.csv").open(
    encoding="utf-8", newline=""
) as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames
    rows = list(reader)

seen = set()
clean_rows = []
exceptions = []

for row in rows:
    row_key = tuple(row[column] for column in columns)

    if row_key in seen:
        exceptions.append({
            **row,
            "issue": "Exact duplicate",
            "action": "Excluded extra copy",
        })
        continue

    seen.add(row_key)

    total = Decimal(row["total_miles"])
    payable = Decimal(row["payable_miles"])

    if total <= 0 or payable < 0 or payable > total:
        exceptions.append({
            **row,
            "issue": "Invalid mileage",
            "action": "Excluded pending source review",
        })
        continue

    if not row["beacon_detection_pct"].strip():
        exceptions.append({
            **row,
            "issue": "Missing beacon detection",
            "action": "Kept for mileage analysis; omit from beacon comparisons",
        })

    clean_rows.append(row)

for filename, fieldnames, output_rows in [
    ("clean_trips.csv", columns, clean_rows),
    ("trip_exceptions.csv", [*columns, "issue", "action"], exceptions),
]:
    with (project / filename).open(
        "w", encoding="utf-8", newline=""
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

print(f"Input rows: {len(rows)}")
print(f"Clean trips: {len(clean_rows)}")
print(f"Exceptions logged: {len(exceptions)}")