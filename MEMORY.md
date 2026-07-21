# SpendDNA - Project Memory

# Project Overview

SpendDNA is a professional financial analytics project that analyzes bank transaction data and generates meaningful financial insights through a structured notebook-based data pipeline.

Each notebook has a single responsibility, consumes the output of the previous notebook, and exports a processed dataset for the next stage.

---

# Project Structure

SpendDNA/
│
├── Assets/
│
├── Config/
│   ├── __init__.py
│   ├── paths.py
│   └── constants.py
│
├── Data/
│   ├── raw_data.pkl
│   ├── cleaned_data.pkl
│   └── (future pipeline outputs)
│
├── Dataset/
│   ├── raw/
│   ├── processed/
│   └── exported/
│
├── Documents/
│   └── SpendDNA.pdf
│
├── Notebooks/
│   ├── 01_Dataset_Exploration.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   └── ...
│
├── Outputs/
│   ├── logs/
│   ├── reports/
│   └── screenshots/
│
├── Utils/
│   ├── __init__.py
│   ├── io.py
│   ├── validation.py
│   ├── cleaning.py
│   ├── analysis.py
│   └── display.py
│
├── README.md
├── ROADMAP.md
├── MEMORY.md
└── requirements.txt

---

# Development Rules

- Follow SpendDNA.pdf strictly.
- One notebook = One responsibility.
- Keep notebook cells lightweight.
- Place reusable logic inside Utils.
- Keep project paths inside Config.
- Avoid duplicated code.
- Every notebook must include:
  - Objective
  - Input
  - Processing
  - Validation
  - Export
  - Summary
- Every notebook exports one pickle file for the next notebook.

---

# Notebook Pipeline

01 Dataset Exploration
        ↓
raw_data.pkl

02 Data Cleaning
        ↓
cleaned_data.pkl

03 Vendor Normalization
        ↓
vendor_data.pkl

04 Category Mapping
        ↓
category_data.pkl

05 Spending Overview
        ↓
overview_data.pkl

06 Monthly Trends
        ↓
monthly_data.pkl

07 Time Analysis
        ↓
time_analysis.pkl

08 Anomaly Detection
        ↓
anomaly_data.pkl

09 Financial Archetypes
        ↓
archetype_data.pkl

10 Final Report
        ↓
final_data.pkl

---

# Completed

✅ Project structure created

✅ Config module

✅ Utils module

✅ Shared path management

✅ IO utilities

✅ Validation utilities

✅ Display utilities

✅ Cleaning utilities

✅ Notebook 01 – Dataset Exploration

✅ Notebook 02 – Data Cleaning

---

# Dataset Information

Original Dataset

Rows: 1328

Columns: 8

Columns

- Date
- Time
- Description
- Type
- Amount
- Balance
- Mode
- Ref

---

# Notebook 02 Summary

Input File

- raw_data.pkl

Output File

- cleaned_data.pkl

Processing Performed

- Standardized date formats
- Standardized transaction types
- Cleaned amount values
- Trimmed text columns
- Removed duplicate rows

Output Statistics

Input Rows : 1328

Output Rows : 1310

Duplicates Removed : 18

Columns : 8

---

# Current Status

Current Completed Notebook

Notebook 02 – Data Cleaning

Next Notebook

Notebook 03 – Vendor Normalization

Status

Ready to Begin

---

# Notes

- All intermediate datasets are stored as pickle files inside the Data directory.
- Pickle files contain complete pandas DataFrames and are used as the project's pipeline format.
- CSV exports are optional and intended only for manual inspection or debugging.
- Every notebook must remain independent by loading only the previous notebook's output.