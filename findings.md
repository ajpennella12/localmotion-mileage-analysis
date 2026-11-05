# LocalMotion Mileage Analysis Findings

After validation, the synthetic dataset contained 599 trips.

## Cohort comparison

Established drivers had a higher mileage-weighted payable share within
both app versions.

- Version 1.0 — 79.76% for established drivers and 74.43% for new drivers,
  a gap of 5.33 percentage points.
- Version 1.1 — 89.63% for established drivers and 85.06% for new drivers,
  a gap of 4.57 percentage points.

## Version comparison

Payable-mile share increased by 9.87 percentage points for established
drivers and 10.63 points for new drivers between versions.

## Interpretation and limitations

These patterns reflect assumptions built into the synthetic data
generator. They demonstrate the analysis workflow.

Version 1.0 appears only in January and version 1.1 only in February.
The data cannot distinguish an app-version effect from a month effect.

Payable-mile share is total payable miles divided by total miles.
It is weighted by mileage. The trip with a missing beacon reading
remains included because its mileage passed validation.

## Proposed follow-up

With real operational data, compare versions operating during the same
period and investigate differences in device setup, trip conditions,
and driver onboarding before recommending changes.

## Correlation and regression

Across 599 synthetic trips, the correlation between trip length and
payable-mile share was approximately 0.0003.

A linear regression accounting for app version and driver cohort estimated
a trip-length coefficient of -0.0184 percentage points per mile. Its
conventional p-value was 0.397. This analysis provides little evidence
of a linear trip-length association under the model assumptions.

Version 1.1 was associated with a 10.17 percentage-point higher payable
share, and new-driver status with a 5.22-point lower share. The model
explained 34.6% of the variation in individual trip payable shares.

These results reflect simulated relationships. Version and month change
together, and repeated trips within drivers limit the interpretation of
the model's conventional standard errors and p-values.