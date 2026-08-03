import pandas as pd
import numpy as np


def prepare_hour_column(df):
    """Extract hour from transaction time."""
    data = df.copy()

    data["Hour"] = (
        pd.to_datetime(
            data["Time"],
            format="%H:%M",
            errors="coerce"
        ).dt.hour
    )

    data = data.dropna(subset=["Hour"])

    data["Hour"] = data["Hour"].astype(int)

    return data


def filter_debit_transactions(df):
    """Keep only debit transactions."""

    if "Transaction Type" in df.columns:
        return df[df["Transaction Type"] == "Debit"].copy()

    return df[df["Type"] == "Debit"].copy()


def build_hourly_summary(df):
    """Create hour-wise spending summary."""

    hourly = (
        df.groupby("Hour")["Amount"]
        .sum()
        .reindex(range(24), fill_value=0)
        .reset_index()
    )

    hourly.columns = [
        "Hour",
        "Total Spend"
    ]

    return hourly


def build_category_hour_matrix(df):
    """Create category × hour spending matrix."""

    matrix = pd.pivot_table(
        df,
        index="Category",
        columns="Hour",
        values="Amount",
        aggfunc="sum",
        fill_value=0
    )

    matrix = matrix.reindex(
        columns=range(24),
        fill_value=0
    )

    return matrix


def find_peak_hour(hourly_summary):
    """Find overall peak spending hour."""

    idx = hourly_summary["Total Spend"].idxmax()

    return {
        "Peak Hour": int(hourly_summary.loc[idx, "Hour"]),
        "Amount": float(hourly_summary.loc[idx, "Total Spend"])
    }


def find_category_peak_hours(matrix):
    """Find peak spending hour for each category."""

    result = pd.DataFrame(index=matrix.index)

    result["Peak Hour"] = matrix.idxmax(axis=1)
    result["Peak Spend"] = matrix.max(axis=1)

    return result


def calculate_late_night_spending(df):
    """Analyse spending between 9 PM and 1 AM."""

    late_hours = [21, 22, 23, 0, 1]

    late = df[df["Hour"].isin(late_hours)].copy()

    total = df["Amount"].sum()

    summary = {
        "Late Night Transactions": len(late),
        "Late Night Spend": late["Amount"].sum(),
        "Overall Spend": total,
        "Percentage":
            (
                late["Amount"].sum() / total * 100
            )
            if total > 0
            else 0
    }

    return summary


def print_hourly_bars(hourly_summary):
    """Display ASCII hourly spending bars."""

    maximum = hourly_summary["Total Spend"].max()

    if maximum == 0:
        maximum = 1

    for _, row in hourly_summary.iterrows():

        length = int(
            (row["Total Spend"] / maximum) * 30
        )

        print(
            f"{int(row['Hour']):02d} | "
            + "█" * length
        )


def prepare_metadata(df, matrix):
    """Create metadata."""

    metadata = {
        "total_transactions": len(df),
        "total_categories": matrix.shape[0],
        "total_hours": 24
    }

    return metadata


def generate_time_of_day_patterns(df):
    """Generate complete time-of-day analysis."""

    data = prepare_hour_column(df)
    data = filter_debit_transactions(data)

    hourly_summary = build_hourly_summary(data)

    category_hour_matrix = build_category_hour_matrix(data)

    peak_hour = find_peak_hour(hourly_summary)

    category_peak_hours = find_category_peak_hours(
        category_hour_matrix
    )

    late_night_summary = calculate_late_night_spending(
        data
    )

    metadata = prepare_metadata(
        data,
        category_hour_matrix
    )

    return {
        "hourly_summary": hourly_summary,
        "category_hour_matrix": category_hour_matrix,
        "category_peak_hours": category_peak_hours,
        "late_night_summary": late_night_summary,
        "peak_hour": peak_hour,
        "metadata": metadata
    }