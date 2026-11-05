# LocalMotion Mileage Analysis

A portfolio project using synthetic trip data inspired by the
payable-mile eligibility concept in LocalMotion Endorsements.

## Interactive dashboard

[Explore the Tableau dashboard](https://public.tableau.com/app/profile/alessandro.pennella/viz/LocalMotionMileageAnalysis/LocalMotionMileageAnalysis)

## Tools

Python for data generation, validation, summaries, and charts.
R for correlation and multiple linear regression.
Tableau Public for the interactive cohort comparison.

## Reproduce the analysis

Run these commands from the project folder:

    python3 generate_trips.py
    python3 validate_trips.py
    python3 analyze_trips.py
    Rscript analyze_relationship.R
    python3 prepare_tableau.py

To regenerate the Python chart, install matplotlib and run:

    python3 -m pip install matplotlib
    python3 chart_cohorts.py

## Data validation

The generator creates 601 rows, including three intentional issues.
Validation excludes an exact duplicate and an impossible mileage record,
leaving 599 trips. A trip with missing beacon detection is retained for
mileage analysis and logged for review.

## Findings

| App version | Established drivers | New drivers |
|---|---:|---:|
| 1.0 | 79.76% | 74.43% |
| 1.1 | 89.63% | 85.06% |

These percentages divide total payable miles by total miles within
each group.

Trip length had essentially no linear correlation with individual
trip payable share, with r approximately 0.0003. Regression accounting
for app version and cohort estimated -0.0184 percentage points per
additional mile.

## Limitations

Relationships reflect assumptions in the synthetic generator.
App version changes with month, so their effects cannot be separated.
Repeated trips within drivers limit interpretation of conventional
regression standard errors and p-values.

## Detailed results

See findings.md, cohort_summary.csv, regression_results.txt,
regression_coefficients.csv, and trip_exceptions.csv.