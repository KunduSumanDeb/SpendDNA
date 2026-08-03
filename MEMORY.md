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
| Function 9 - Final SpendDNA Report | ✅ Completed |
| Final Submission | ⏳ Next |

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

final_report.pkl

↓

Final Submission

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
- Late-night Food %
- Subscription Vendor Count
- Savings Rate

Utility

- Utils/archetype.py

Status

✅ Completed

---

## Function 9

Export

- final_report.pkl

Contains

- executive_summary
- top_spending_vendors
- top_frequency_vendors
- monthly_summary
- time_summary
- anomaly_summary
- archetype_summary
- metadata

Utility

- Utils/report.py

Notebook

- 09_Final_Report.ipynb

Status

✅ Completed

Purpose

Generate a consolidated SpendDNA report by combining outputs from Functions 4–8.

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
- report.py

Business logic exists only inside Utils.

Notebooks remain orchestration only.

---

# analysis.py

Current Status

Still intentionally empty.

Reserved for

- End-to-end execution
- Pipeline automation
- Future CLI integration

No implementation unless future requirements demand it.

---

# Architectural Decisions

✓ One notebook = One function

✓ One utility = One responsibility

✓ One export = One pickle

✓ Utilities contain all business logic

✓ Notebooks orchestrate execution only

✓ Preserve backward compatibility

✓ Metadata included in every export

✓ Downstream notebooks consume exported pickle files only

---

# Export Rules

Each completed function exports one pickle.

Each pickle contains

- transactions (when required)
- analysis outputs
- metadata

Never remove keys already consumed by downstream notebooks.

---

# Coding Standards

- Follow PEP-8
- Modular utility functions
- Function docstrings
- Short notebook cells
- Validation before export
- Final summary after each function
- Prefer Python native numeric types over NumPy scalars

---

# Current Project Folder

SpendDNA/

│

├── Data/

│   ├── raw_data.pkl
│   ├── cleaned_data.pkl
│   ├── vendor_data.pkl
│   ├── merchant_summary.pkl
│   ├── monthly_trends.pkl
│   ├── time_of_day_patterns.pkl
│   ├── anomaly_detection.pkl
│   ├── spending_archetypes.pkl
│   └── final_report.pkl

│

├── Utils/

│   ├── io.py
│   ├── cleaning.py
│   ├── vendor.py
│   ├── merchant.py
│   ├── monthly_trends.py
│   ├── time_of_day.py
│   ├── anomaly_detection.py
│   ├── archetype.py
│   └── report.py

│

├── Notebooks/

│   ├── 01_Data_Ingestion.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Vendor_Normalization.ipynb
│   ├── 04_Merchant_Insights.ipynb
│   ├── 05_Monthly_Trend_Analysis.ipynb
│   ├── 06_Time_of_Day_Analysis.ipynb
│   ├── 07_Anomaly_Detection.ipynb
│   ├── 08_Spending_Archetypes.ipynb
│   └── 09_Final_Report.ipynb

---

# Remaining Work (Final Submission)

The analytical pipeline is complete.

Remaining deliverables are project submission components:

- Three data-specific insights
- Reflection section
- AI assistance disclosure
- README.md
- Screenshot-ready formatted report
- GitHub repository cleanup
- Final documentation

No further analytical utilities are required unless optional bonus features are implemented.

---

# Known Future Improvements (Optional)

- Vendor-to-category mapping refinement
- Weekend vs Weekday analysis
- Rolling 3-month spend forecasting
- Invented archetype
- Vendor cleanup audit
- Streamlit dashboard
- analysis.py as end-to-end pipeline runner

These are optional enhancements and do not affect the completed modular architecture.