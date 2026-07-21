"""
Project path configuration for SpendDNA.

This module centralizes all directory and file paths used
throughout the project.
"""

from pathlib import Path

# Project Root

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# Project Directories

ASSETS_DIR = PROJECT_ROOT / "Assets"
CONFIG_DIR = PROJECT_ROOT / "Config"
DATA_DIR = PROJECT_ROOT / "Data"
DATASET_DIR = PROJECT_ROOT / "Dataset"
DOCUMENTS_DIR = PROJECT_ROOT / "Documents"
NOTEBOOKS_DIR = PROJECT_ROOT / "Notebooks"
OUTPUTS_DIR = PROJECT_ROOT / "Outputs"
UTILS_DIR = PROJECT_ROOT / "Utils"


# Dataset Directories

RAW_DATASET_DIR = DATASET_DIR / "raw"
PROCESSED_DATASET_DIR = DATASET_DIR / "processed"
EXPORTED_DATASET_DIR = DATASET_DIR / "exported"


# Output Directories

LOGS_DIR = OUTPUTS_DIR / "logs"
REPORTS_DIR = OUTPUTS_DIR / "reports"
SCREENSHOTS_DIR = OUTPUTS_DIR / "screenshots"


# Data Files

RAW_DATASET = RAW_DATASET_DIR / "Dataset_Raw.csv"

RAW_DATA_PKL = DATA_DIR / "raw_data.pkl"
CLEANED_DATA_PKL = DATA_DIR / "cleaned_data.pkl"
VENDOR_DATA_PKL = DATA_DIR / "vendor_data.pkl"
CATEGORY_DATA_PKL = DATA_DIR / "category_data.pkl"
OVERVIEW_DATA_PKL = DATA_DIR / "overview_data.pkl"
MONTHLY_DATA_PKL = DATA_DIR / "monthly_data.pkl"
TIME_ANALYSIS_PKL = DATA_DIR / "time_analysis.pkl"
ANOMALY_DATA_PKL = DATA_DIR / "anomaly_data.pkl"
ARCHETYPE_DATA_PKL = DATA_DIR / "archetype_data.pkl"
FINAL_DATA_PKL = DATA_DIR / "final_data.pkl"