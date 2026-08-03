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
| Function 8 - Spending Archetype Detection | ✅ Completed |
| Function 9 - Final SpendDNA Report | ⏳ Next |

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

spending_archetypes.pkl

↓

Function 9

↓

Final SpendDNA Report

---

# Function Outputs

## Function 1

Export

- raw_data.pkl

Purpose

- Load dataset
- Initial validation
- Preserve original data

---

## Function 2

Export

- cleaned_data.pkl

Purpose

- Clean records
- Standardize values
- Remove invalid rows

---

## Function 3

Export

- vendor_data.pkl

Purpose

- Vendor normalization
- Category tagging

Final Columns

- Date
- Time
- Description
- Transaction Type
- Amount
- Balance
- Mode
- Ref
- Vendor
- Category

---

## Function 4

Export

- merchant_summary.pkl

Contains

- transactions
- merchant_summary
- merchant_category
- monthly_summary
- top_spend
- top_frequency
- metadata

---

## Function 5

Export

- monthly_trends.pkl

Contains

- transactions
- monthly_pivot
- monthly_totals
- monthly_changes
- growth_summary
- decline_summary
- metadata

---

## Function 6

Export

- time_of_day_patterns.pkl

Contains

- transactions
- hourly_summary
- category_hour_matrix
- category_peak_hours
- late_night_summary
- peak_hour
- metadata

---

## Function 7

Export

- anomaly_detection.pkl

Contains

- transactions
- category_statistics
- transactions_with_zscore
- anomalies
- top_anomalies
- metadata

Notes

- Debit-only anomaly detection
- Z-score threshold = 2

---

## Function 8

Export

- spending_archetypes.pkl

Contains

- transactions
- archetype_results
- matched_archetypes
- archetype_summary
- metadata

Implemented Archetypes

- THE FOODIE
- THE QUICK COMMERCE JUNKIE
- THE SHOPAHOLIC
- THE INVESTOR
- THE LATE-NIGHT SNACKER
- THE CAB COMMUTER
- THE SUBSCRIPTION LOVER
- THE YOLO SPENDER
- THE DISCIPLINED SAVER

Implemented Metrics

- Food %
- Quick Commerce %
- E-commerce %
- Investment %
- Transport %
- Late-night food %
- Subscription vendor count
- Savings rate

Utility

- Utils/archetype.py

Status

✅ Completed

---

# Utilities

Current utilities

- io.py
- cleaning.py
- vendor.py
- merchant.py
- monthly_trends.py
- time_of_day.py
- anomaly_detection.py
- archetype.py

Business logic exists only inside Utils.

Notebooks remain orchestration only.

---

# analysis.py

Still intentionally empty.

Reserved for

- Final project pipeline
- Future automation
- End-to-end execution

---

# Architectural Decisions

✓ One notebook = One function

✓ One utility = One responsibility

✓ One export = One pickle

✓ Utilities contain business logic

✓ Notebook only orchestrates execution

✓ Preserve backward compatibility

✓ Export transactions whenever required

✓ Metadata included in every export

---

# Export Rules

Each function exports exactly one pickle.

Each pickle contains

- transactions (when needed)
- outputs
- metadata

Never remove keys already consumed by downstream notebooks.

---

# Coding Standards

- PEP-8
- Short cells
- Function docstrings
- Validation before export
- Print summary
- Native Python types preferred over NumPy scalars

---

# Known Improvements

Future

Vendor categorization can later be expanded without changing architecture.

Current project already supports downstream compatibility.

---

# Remaining Functions

## Function 9

Purpose

Generate the final SpendDNA console report.

Inputs

- merchant_summary.pkl
- monthly_trends.pkl
- time_of_day_patterns.pkl
- anomaly_detection.pkl
- spending_archetypes.pkl

Expected Sections

1 Executive Summary

2 Top Categories

3 Top Vendors

4 Time-of-Day Patterns

5 Monthly Trend

6 Top Anomalies

7 Spending Archetypes

8 Key Insights

Export

- final_report.pkl

Utility

- report.py

Notebook

09_Final_Report.ipynb

---

# Project Folder

SpendDNA/

│

├── Data/

├── Utils/

│ ├── io.py

│ ├── cleaning.py

│ ├── vendor.py

│ ├── merchant.py

│ ├── monthly_trends.py

│ ├── time_of_day.py

│ ├── anomaly_detection.py

│ ├── archetype.py

│ └── report.py (next)

│

├── Notebooks/

│ ├── 01_Data_Ingestion.ipynb

│ ├── 02_Data_Cleaning.ipynb

│ ├── 03_Vendor_Normalization.ipynb

│ ├── 04_Merchant_Insights.ipynb

│ ├── 05_Monthly_Trend_Analysis.ipynb

│ ├── 06_Time_of_Day_Analysis.ipynb

│ ├── 07_Anomaly_Detection.ipynb

│ ├── 08_Spending_Archetypes.ipynb

│ └── 09_Final_Report.ipynb

---

# Next Task

Begin Function 9.

The objective is to generate the formatted SpendDNA report exactly in the style shown in Section 11 of the project PDF.

The report should include:

- Executive Summary
- Top Categories
- Top Vendors
- Time-of-Day Patterns
- Monthly Trend
- Top Anomalies
- Spending Archetypes
- Key Insights

One utility

Utils/report.py

One notebook

09_Final_Report.ipynb

One export

final_report.pkl

No previous notebook should require modification.