# SpendDNA - Project Memory

Last Updated: 22 July 2026

---

# Project Status

## Overall Progress

| Function | Status |
|----------|--------|
| Function 1 - Data Ingestion | ✅ Completed |
| Function 2 - Data Cleaning | ✅ Completed |
| Function 3 - Vendor Normalization | ✅ Completed |
| Function 4 - Merchant Insights | ✅ Completed |
| Function 5 | ⏳ Pending |

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
Function 5 ...

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
datetime64
```

using

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

# Utility Reuse

Current utilities reused

- Utils/io.py
- Utils/vendor.py
- Utils/merchant.py

Avoid rewriting utility functions unless absolutely necessary.

---

# Important Decisions

✓ One notebook = One function

✓ Every notebook exports one pickle

✓ Preserve modular pipeline

✓ Never duplicate business logic

✓ Utilities remain the single source of truth

✓ Notebook only orchestrates processing

---

# Known Improvements

Transaction Type should be normalized to uppercase in Function 3.

Recommended implementation

```python
vendor_data["Transaction Type"] = (
    vendor_data["Transaction Type"]
    .astype(str)
    .str.upper()
)
```

This maintains compatibility with utility filters.

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

Function 5

---

# Next Task

Implement Function 5 while

- following existing architecture
- reusing utilities
- exporting a single pickle
- avoiding code duplication
- preserving compatibility with Functions 1–4