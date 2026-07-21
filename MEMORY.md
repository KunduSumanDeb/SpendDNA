# SpendDNA - Project Memory

## Project Overview

SpendDNA is a professional financial analytics project that analyzes bank transaction data and generates meaningful financial insights through a structured data pipeline.

The project follows a notebook-based workflow where each notebook has a single responsibility and exports its output for the next stage.

---

# Project Structure

SpendDNA/
│
├── Assets/
├── Config/
│   ├── __init__.py
│   ├── paths.py
│   └── constants.py
│
├── Data/
│   ├── raw_data.pkl
│   └── (future exported pickle files)
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
- Every notebook has:
    - Objective
    - Input
    - Processing
    - Validation
    - Export
    - Summary
- Reusable logic belongs inside Utils.
- Project paths belong inside Config.
- Avoid duplicated code.
- Maintain clean documentation.
- Every notebook exports a pickle file for the next notebook.

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

✅ Config module created

✅ Utils module created

✅ Shared path management

✅ Shared IO utilities

✅ Shared validation utilities

✅ Shared display utilities

✅ Notebook 01 completed

---

# Dataset Information

Rows:
1328

Columns:
8

Columns

- Date
- Time
- Description
- Type
- Amount
- Balance
- Mode
- Ref

Validation

Missing Values : 0

Duplicate Rows : 18

---

# Current Status

Current Completed Notebook

Notebook 01

Next Notebook

Notebook 02
Data Cleaning

Status

Ready to Begin