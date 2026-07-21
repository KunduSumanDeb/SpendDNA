# SpendDNA Project Memory

## Project Status

### Completed Functions

- ✅ Function 1 – Data Cleaning & Standardization
- ✅ Function 2 – Transaction Categorization
- ✅ Function 3 – Vendor Normalization

Current Progress: **3 / 8 Functions Completed**

---

# Project Architecture

## Folder Structure

SpendDNA/
│
├── Config/
│   └── paths.py
│
├── Data/
│   ├── Raw/
│   ├── Processed/
│   └── Outputs/
│
├── Utils/
│   ├── cleaning.py
│   ├── categorization.py
│   ├── vendor.py
│   └── ...
│
├── Notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_Transaction_Categorization.ipynb
│   ├── 03_Vendor_Normalization.ipynb
│   └── ...
│
└── memory.md

---

# Notebook Development Rules

Every notebook follows the same structure:

1. Markdown Title
2. Code Cell 1 – Setup
3. Code Cell 2 – Imports
4. Code Cell 3 – Load Dataset
5. Code Cell 4 – Processing
6. Code Cell 5 – Validation
7. Code Cell 6 – Export
8. Markdown Summary

---

# Utility Module Rules

- Heavy logic remains inside `Utils/`.
- Notebooks should only orchestrate function calls.
- Every utility function must include a docstring.
- Keep functions modular and reusable.
- Avoid duplicate logic across utilities.

---

# Configuration Rules

Always use paths from:

Config/paths.py

Do not hardcode file paths.

---

# Function 3 Summary

Notebook:
03_Vendor_Normalization.ipynb

Utility:
Utils/vendor.py

Input:

- cleaned_data.pkl

Output:

- vendor_data.pkl

Processing:

- Vendor extraction
- Prefix removal
- Special character cleaning
- UPI ID removal
- Reference (REF/UTR/TXN) removal
- Merchant normalization
- Vendor dataset creation

Normalization Features:

- Large KNOWN_BRANDS mapping
- Longest-keyword matching
- Alias normalization
- Generic vendor cleaning
- Unknown vendor fallback

Validation Results

Total Transactions : 1310

Unique Vendors : 64

Top Vendors

- SWIGGY
- ZOMATO
- OLA
- AMAZON
- ZEPTO
- UBER
- BLINKIT
- RAPIDO
- FLIPKART
- STARBUCKS

Status:

✅ Function 3 Completed

---

# Coding Standards

- One notebook = One function
- Validate before exporting
- Export only pickle files
- Keep notebooks clean
- No duplicated cells
- Reusable utilities only
- Follow modular architecture
- Maintain consistent naming conventions

---

# Next Function

Function 4

Merchant Insights

Planned Utility:

Utils/merchant.py

Planned Notebook:

04_Merchant_Insights.ipynb

Expected Output:

merchant_summary.pkl