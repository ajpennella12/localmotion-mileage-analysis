trips <- read.csv("clean_trips.csv")
trips$payable_share_pct <- trips$payable_miles / trips$total_miles * 100

# Treat version and cohort as categories.
trips$app_version <- factor(trips$app_version)
trips$driver_cohort <- factor(trips$driver_cohort)

correlation <- cor(trips$total_miles, trips$payable_share_pct)

# Estimate the trip-length association while accounting for the groups.
model <- lm(
  payable_share_pct ~ total_miles + app_version + driver_cohort,
  data = trips
)

capture.output(
  cat("Synthetic LocalMotion mileage analysis\n\n"),
  cat("Trips analyzed:", nrow(trips), "\n"),
  cat("Trip length and payable-share correlation:", correlation, "\n\n"),
  print(summary(model)),
  cat(
    "\nLimitations\n",
    "App version changes with month, so their effects cannot be separated.\n",
    "Trips repeat within drivers; standard model errors assume independence.\n",
    "Relationships reflect assumptions in the synthetic generator.\n",
    file = ""
  ),
  file = "regression_results.txt"
)

coefficients <- as.data.frame(coef(summary(model)))
coefficients$term <- rownames(coefficients)
rownames(coefficients) <- NULL
write.csv(coefficients, "regression_coefficients.csv", row.names = FALSE)

cat("Created regression_results.txt and regression_coefficients.csv\n")
cat("Trip length and payable-share correlation:", round(correlation, 4), "\n")