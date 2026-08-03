import pandas as pd
import numpy as np


def prepare_month_column(df):
    """Extract month from transaction date."""
    data = df.copy()
    data["Month"] = data["Date"].dt.strftime("%b")
    return data


def filter_debit_transactions(df):
    """Keep only debit transactions."""
    return df[df["Transaction Type"] == "Debit"].copy()

def build_monthly_pivot(df):
    """Create category-wise monthly spending table."""
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    pivot = pd.pivot_table(
        df,
        index="Category",
        columns="Month",
        values="Amount",
        aggfunc="sum",
        fill_value=0
    )

    pivot = pivot.reindex(columns=month_order, fill_value=0)

    return pivot


def calculate_monthly_totals(pivot):
    """Calculate total spending for each month."""
    return pivot.sum(axis=0)


def calculate_monthly_changes(pivot):
    """Calculate month-on-month spending changes."""
    return pivot.diff(axis=1).fillna(0)


def find_growth_decline(changes):
    """Find highest monthly growth and decline."""

    growth_summary = pd.DataFrame({
        "Highest Growth": changes.max(axis=1),
        "Growth Month": changes.idxmax(axis=1)
    })

    decline_summary = pd.DataFrame({
        "Highest Decline": changes.min(axis=1),
        "Decline Month": changes.idxmin(axis=1)
    })

    return growth_summary, decline_summary


def prepare_metadata(df, pivot):
    """Create metadata for the analysis."""

    metadata = {
        "total_transactions": len(df),
        "total_categories": pivot.shape[0],
        "total_months": pivot.shape[1]
    }

    return metadata


def generate_monthly_trends(df):
    """Generate monthly spending analysis."""

    data = prepare_month_column(df)
    data = filter_debit_transactions(data)

    monthly_pivot = build_monthly_pivot(data)
    monthly_totals = calculate_monthly_totals(monthly_pivot)
    monthly_changes = calculate_monthly_changes(monthly_pivot)

    growth_summary, decline_summary = find_growth_decline(monthly_changes)

    metadata = prepare_metadata(data, monthly_pivot)

    return {
        "monthly_pivot": monthly_pivot,
        "monthly_totals": monthly_totals,
        "monthly_changes": monthly_changes,
        "growth_summary": growth_summary,
        "decline_summary": decline_summary,
        "metadata": metadata
    }

