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
| Function 7 | ⏳ Pending |

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

Converted to

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

Generate merchant-level spending analytics from normalized vendors.

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

Generate category-wise monthly spending trends and identify month-on-month growth and decline.

Status

Validated successfully.

Notes

- Uses debit transactions for spending analysis.
- Produces monthly pivot tables for downstream reporting.
- Exports the processed transaction dataset for downstream functions.
- Current output contains one category (`Uncategorized`) because category mapping is not yet finalized.

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

Analyze spending behaviour across different hours of the day.

Features

- Hour extraction
- Hour-wise spending
- Category-wise hourly spending
- Peak spending hour
- Peak hour by category
- Late-night spending analysis

Status

Validated successfully.

Current Results

- Transactions analysed: 1304
- Hours analysed: 24
- Peak spending hour identified successfully.
- Late-night spending summary generated successfully.

Notes

- Category count is currently 1 because all transactions belong to the default category (`Uncategorized`).
- Utility returns NumPy numeric types. These can later be converted to Python native types for cleaner summaries if required.

---

# Utility Reuse

Current utilities

- Utils/io.py
- Utils/vendor.py
- Utils/merchant.py
- Utils/monthly_trends.py
- Utils/time_of_day.py

Utilities are the only location containing business logic.

Notebooks only orchestrate execution.

---

# analysis.py

Current Status

- File exists.
- No implementation yet.
- Has not been required by Functions 1–6.

Decision

Leave empty until the complete pipeline is implemented.

Possible future role

- Pipeline runner
- End-to-end analysis orchestrator

No implementation unless required by the project specification.

---

# Important Decisions

✓ One notebook = One function

✓ Every notebook exports one pickle

✓ Preserve modular architecture

✓ Never duplicate business logic

✓ Utilities remain the single source of truth

✓ Notebook only orchestrates processing

✓ Every downstream notebook loads exactly one pickle

✓ Transaction dataset is preserved for downstream compatibility

---

# Known Improvements

## Category Mapping

Current category value

```
Uncategorized
```

Future improvement

Implement automatic merchant-to-category mapping.

---

## Transaction Type

Normalize to uppercase.

Recommended implementation

```python
vendor_data["Transaction Type"] = (
    vendor_data["Transaction Type"]
    .astype(str)
    .str.upper()
)
```

---

## NumPy Scalar Types

Convert exported NumPy numeric values to Python native types where appropriate.

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

Function 7

---

# Next Task

Before implementing Function 7

- Review Function 7 requirements from SpendDNA.pdf.
- Verify required inputs and outputs.
- Confirm whether Function 6 exports everything needed.
- Review remaining pipeline (Functions 7–10).
- Decide final role of analysis.py.
- Reuse existing utilities whenever possible.
- Avoid modifying completed functions unless necessary.


# Next Task

Before implementing Function 7

- Review Function 7 requirements from SpendDNA.pdf.
- Verify required inputs and outputs.
- Confirm whether Function 6 exports everything needed.
- Review remaining pipeline (Functions 7–10).
- Decide final role of analysis.py.
- Reuse existing utilities whenever possible.
- Avoid modifying completed functions unless necessary.

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

- One utility file per function.
- Business logic only inside Utils.
- Notebooks should never contain processing logic.
- Every utility function must include a docstring.
- Reuse existing utilities whenever possible.

---

## Export Rules

- Every function exports exactly one pickle.
- Export transactions when required downstream.
- Export function-specific outputs.
- Export metadata.
- Never remove existing keys from completed functions.
- Only add new keys if required for downstream compatibility.

---

## Naming Convention

### Notebooks

01_Data_Ingestion.ipynb
02_Data_Cleaning.ipynb
03_Vendor_Normalization.ipynb
04_Merchant_Insights.ipynb
05_Monthly_Trend_Analysis.ipynb
06_Time_of_Day_Analysis.ipynb

### Utilities

io.py
cleaning.py
vendor.py
merchant.py
monthly_trends.py
time_of_day.py

### Export Files

raw_data.pkl
cleaned_data.pkl
vendor_data.pkl
merchant_summary.pkl
monthly_trends.pkl
time_of_day_patterns.pkl

---

## Coding Standards

- Follow PEP-8.
- Keep notebooks clean and readable.
- Use short comments describing each cell.
- Avoid unnecessary blank lines.
- Keep variable names meaningful.
- Validate outputs before exporting.
- Print a final summary after every function.

---

## Architectural Principles

- One notebook = One function
- One utility = One responsibility
- One export = One pickle
- Utilities contain business logic
- Notebooks orchestrate execution
- Preserve backward compatibility
- Never rewrite completed functions unless absolutely necessary
- Review downstream dependencies before starting a new function
- Keep pipeline modular and reusable