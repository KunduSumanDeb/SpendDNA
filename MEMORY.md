# SpendDNA - Project Memory

Last Updated: 03 August 2026

---

# Project Status

## Overall Progress

| Function | Status |
|----------|--------|
| Function 1 - Data Ingestion | ✅ Completed |
| Function 2 - Data Cleaning | ✅ Completed |
| Function 3 - Vendor Normalization | ✅ Completed |
| Function 4 - Merchant Insights | ✅ Completed |
| Function 5 - Monthly Trend Analysis | ✅ Completed |
| Function 6 - Time-of-Day Analysis | ✅ Completed |
| Function 7 - Anomaly Detection | ✅ Completed |

---

# Current Architecture

Raw Data

↓

Function 1

↓

raw_data.pkl

↓

Function 2

↓

cleaned_data.pkl

↓

Function 3

↓

vendor_data.pkl

↓

Function 4

↓

merchant_summary.pkl

↓

Function 5

↓

monthly_trends.pkl

↓

Function 6

↓

time_of_day_patterns.pkl

↓

Function 7

↓

anomaly_detection.pkl

↓

Function 8

---

# Completed Outputs

## Function 1

Exports

- raw_data.pkl

Purpose

- Load raw transaction data
- Perform initial validation
- Preserve original dataset

---

## Function 2

Exports

- cleaned_data.pkl

Purpose

- Remove invalid records
- Standardize transaction fields
- Produce cleaned dataset

---

## Function 3

Exports

- vendor_data.pkl

Purpose

- Normalize merchant/vendor names
- Prepare dataset for merchant analytics

Final Schema

| Column |
|---------|
| Date |
| Time |
| Description |
| Transaction Type |
| Amount |
| Balance |
| Mode |
| Ref |
| Vendor |
| Category |

Important Fixes

### Transaction Type

Original

```
Type
```

Renamed to

```
Transaction Type
```

### Date

Converted using

```python
pd.to_datetime(...)
```

### Category

Added

```
Category
```

Default value

```
Uncategorized
```

---

## Function 4

Exports

- merchant_summary.pkl

Generated Outputs

- merchant_summary
- merchant_category
- monthly_summary
- top_spend
- top_frequency
- metadata

Purpose

Generate merchant-level spending analytics.

Status

Validated successfully.

---

## Function 5

Exports

- monthly_trends.pkl

Generated Outputs

- transactions
- monthly_pivot
- monthly_totals
- monthly_changes
- growth_summary
- decline_summary
- metadata

Purpose

Generate monthly spending trends.

Status

Validated successfully.

Notes

- Debit transactions used.
- Transactions exported for downstream functions.

---

## Function 6

Exports

- time_of_day_patterns.pkl

Generated Outputs

- transactions
- hourly_summary
- category_hour_matrix
- category_peak_hours
- late_night_summary
- peak_hour
- metadata

Purpose

Analyze spending behaviour across different hours.

Features

- Hour extraction
- Hour-wise spending
- Category-wise hourly spending
- Peak hour detection
- Late-night spending analysis

Status

Validated successfully.

---

## Function 7

Exports

- anomaly_detection.pkl

Generated Outputs

- transactions
- category_statistics
- transactions_with_zscore
- anomalies
- top_anomalies
- metadata

Purpose

Detect anomalous spending transactions using Z-score analysis.

Features

- Category statistics
- Z-score computation
- Debit-only anomaly detection
- Top anomaly extraction
- Metadata generation

Status

Validated successfully.

Current Results

- Transactions analysed: 1310
- Categories: 1
- Total anomalies: 50
- Threshold: 2.0

Notes

- Only debit transactions are considered for anomaly detection.
- Credit transactions are excluded from anomaly detection.
- Current category count remains 1 because vendor categorization is not yet implemented.

---

# Utility Reuse

Current utilities

- Utils/io.py
- Utils/vendor.py
- Utils/merchant.py
- Utils/monthly_trends.py
- Utils/time_of_day.py
- Utils/anomaly_detection.py

Utilities remain the only location containing business logic.

Notebooks only orchestrate execution.

---

# analysis.py

Current Status

- File exists.
- Still intentionally empty.
- No requirement through Functions 1–7.

Decision

Keep empty until the final pipeline is assembled.

Possible future role

- End-to-end pipeline runner
- Complete SpendDNA report generator
- Single entry-point analysis module

---

# Important Decisions

✓ One notebook = One function

✓ One utility = One responsibility

✓ One export = One pickle

✓ Utilities contain business logic

✓ Notebooks orchestrate execution

✓ Every downstream notebook loads one pickle

✓ Preserve backward compatibility

✓ Export transactions whenever required downstream

---

# Known Improvements

## Category Mapping

Current value

```
Uncategorized
```

Future improvement

Implement automatic vendor-to-category mapping.

This will improve

- Merchant Insights
- Monthly Trends
- Time-of-Day Analysis
- Anomaly Detection

without changing project architecture.

---

## Transaction Type

Normalize to uppercase.

Recommended

```python
vendor_data["Transaction Type"] = (
    vendor_data["Transaction Type"]
    .astype(str)
    .str.upper()
)
```

---

## NumPy Scalar Types

Convert exported NumPy values into native Python types where appropriate.

Example

```python
float(value)
int(value)
```

---

# Current Pipeline

Raw Data

↓

raw_data.pkl

↓

cleaned_data.pkl

↓

vendor_data.pkl

↓

merchant_summary.pkl

↓

monthly_trends.pkl

↓

time_of_day_patterns.pkl

↓

anomaly_detection.pkl

↓

Function 8

---

# Next Task

Before implementing Function 8

- Review Function 8 requirements from SpendDNA.pdf.
- Identify required inputs and outputs.
- Verify whether Function 7 exports everything needed.
- Design the new utility.
- Reuse existing utilities wherever possible.
- Preserve backward compatibility.
- Export exactly one pickle.

---

# Project Conventions

## Notebook Structure

1. Markdown
2. Setup
3. Imports
4. Load Previous Output
5. Execute Analysis
6. Display Results
7. Validation
8. Export Results
9. Summary

---

## Utility Design

- One utility per function
- Business logic only inside Utils
- Every function includes a docstring
- Reuse existing utilities whenever possible

---

## Export Rules

- One function = One pickle
- Export transactions when required downstream
- Export metadata
- Never remove existing exported keys
- Only add keys required for future compatibility

---

## Naming Convention

### Notebooks

01_Data_Ingestion.ipynb

02_Data_Cleaning.ipynb

03_Vendor_Normalization.ipynb

04_Merchant_Insights.ipynb

05_Monthly_Trend_Analysis.ipynb

06_Time_of_Day_Analysis.ipynb

07_Anomaly_Detection.ipynb

### Utilities

io.py

cleaning.py

vendor.py

merchant.py

monthly_trends.py

time_of_day.py

anomaly_detection.py

### Export Files

raw_data.pkl

cleaned_data.pkl

vendor_data.pkl

merchant_summary.pkl

monthly_trends.pkl

time_of_day_patterns.pkl

anomaly_detection.pkl

---

## Coding Standards

- Follow PEP-8
- Keep notebooks clean
- Use short cell comments
- Avoid unnecessary blank lines
- Use meaningful variable names
- Validate before exporting
- Print a summary after every function

---

## Architectural Principles

- One notebook = One function
- One utility = One responsibility
- One export = One pickle
- Utilities contain business logic
- Notebooks orchestrate execution
- Preserve backward compatibility
- Never rewrite completed functions unless necessary
- Review downstream dependencies before starting a new function
- Keep the pipeline modular and reusable