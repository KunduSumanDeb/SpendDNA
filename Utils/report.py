import pandas as pd
import numpy as np


def format_currency(value):
    """
    Format numeric value as Indian Rupee.
    """

    if pd.isna(value):
        value = 0

    return f"₹{float(value):,.2f}"


def ascii_bar(value, maximum, width=20):
    """
    Create an ASCII bar proportional to the value.
    """

    if maximum <= 0:
        return ""

    length = int(
        round((value / maximum) * width)
    )

    return "#" * length


def safe_value(data, key, default=None):
    """
    Safely retrieve a value from a dictionary.
    """

    if isinstance(data, dict):
        return data.get(key, default)

    return default


def dataframe_to_records(df):
    """
    Convert DataFrame to list of dictionaries.
    """

    if isinstance(df, pd.DataFrame):
        return df.to_dict(
            orient="records"
        )

    return []


def first_row(df):
    """
    Return first row as dictionary.
    """

    if (
        isinstance(df, pd.DataFrame)
        and not df.empty
    ):
        return df.iloc[0].to_dict()

    return {}

def prepare_executive_summary(
    merchant_data,
    anomaly_data,
    archetype_data,
    time_data
):
    """
    Prepare executive summary for the report.
    """

    merchant_summary = safe_value(
        merchant_data,
        "merchant_summary",
        pd.DataFrame()
    )

    transactions = safe_value(
        anomaly_data,
        "transactions",
        pd.DataFrame()
    )

    anomalies = safe_value(
        anomaly_data,
        "anomalies",
        pd.DataFrame()
    )

    matched = safe_value(
        archetype_data,
        "matched_archetypes",
        []
    )

    peak_hour = safe_value(
        time_data,
        "peak_hour",
        {}
    )

    summary = {
        "Total Transactions": len(transactions),
        "Unique Vendors": len(merchant_summary),
        "Total Anomalies": len(anomalies),
        "Matched Archetypes": len(matched),
        "Peak Spending Hour": peak_hour
    }

    return summary

def prepare_category_summary(merchant_data):
    """
    Prepare category-wise spending summary.
    """

    category = safe_value(
        merchant_data,
        "merchant_category",
        pd.DataFrame()
    )

    if category.empty:
        return pd.DataFrame()

    summary = category.copy()

    amount_column = summary.columns[-1]

    maximum = summary[amount_column].max()

    summary["Bar"] = summary[
        amount_column
    ].apply(
        lambda x: ascii_bar(
            x,
            maximum
        )
    )

    summary["Formatted Amount"] = summary[
        amount_column
    ].apply(
        format_currency
    )

    return summary

def prepare_top_spending_vendors(
    merchant_data,
    top_n=10
):
    """
    Prepare top spending vendors section.
    """

    vendors = safe_value(
        merchant_data,
        "top_spend",
        pd.DataFrame()
    )

    if vendors.empty:
        return pd.DataFrame()

    summary = (
        vendors
        .head(top_n)
        .copy()
    )

    maximum = summary["Total_Spend"].max()

    summary["Bar"] = summary[
        "Total_Spend"
    ].apply(
        lambda x: ascii_bar(
            x,
            maximum
        )
    )

    summary["Formatted Total"] = summary[
        "Total_Spend"
    ].apply(
        format_currency
    )

    return summary

def prepare_top_frequency_vendors(
    merchant_data,
    top_n=10
):
    """
    Prepare most frequently used vendors section.
    """

    vendors = safe_value(
        merchant_data,
        "top_frequency",
        pd.DataFrame()
    )

    if vendors.empty:
        return pd.DataFrame()

    summary = (
        vendors
        .head(top_n)
        .copy()
    )

    maximum = summary["Transactions"].max()

    summary["Bar"] = summary[
        "Transactions"
    ].apply(
        lambda x: ascii_bar(
            x,
            maximum
        )
    )

    return summary

def prepare_monthly_summary(monthly_data):
    """
    Prepare monthly spending summary.
    """

    totals = safe_value(
        monthly_data,
        "monthly_totals",
        pd.Series(dtype=float)
    )

    if totals.empty:
        return pd.DataFrame()

    summary = (
        totals
        .reset_index()
    )

    summary.columns = [
        "Month",
        "Total_Spend"
    ]

    maximum = summary[
        "Total_Spend"
    ].max()

    summary["Bar"] = summary[
        "Total_Spend"
    ].apply(
        lambda x: ascii_bar(
            x,
            maximum
        )
    )

    summary["Formatted Total"] = summary[
        "Total_Spend"
    ].apply(
        format_currency
    )

    return summary

def prepare_time_summary(time_data):
    """
    Prepare time-of-day spending summary.
    """

    peak = safe_value(
        time_data,
        "peak_hour",
        {}
    )

    if not peak:
        return {}

    summary = {
        "Peak Hour": safe_value(
            peak,
            "Peak Hour",
            "N/A"
        ),
        "Peak Amount": format_currency(
            safe_value(
                peak,
                "Amount",
                0.0
            )
        )
    }

    return summary

def prepare_anomaly_summary(
    anomaly_data,
    top_n=10
):
    """
    Prepare anomaly summary.
    """

    anomalies = safe_value(
        anomaly_data,
        "top_anomalies",
        pd.DataFrame()
    )

    if anomalies.empty:
        return pd.DataFrame()

    summary = (
        anomalies
        .head(top_n)
        .copy()
    )

    if "Amount" in summary.columns:
        summary["Formatted Amount"] = (
            summary["Amount"]
            .apply(format_currency)
        )

    return summary

def prepare_archetype_summary(
    archetype_data
):
    """
    Prepare spending archetype summary.
    """

    matched = safe_value(
        archetype_data,
        "matched_archetypes",
        []
    )

    if len(matched) == 0:
        return pd.DataFrame()

    summary = pd.DataFrame(
        matched
    )

    return summary

def build_report(
    merchant_data,
    monthly_data,
    time_data,
    anomaly_data,
    archetype_data
):
    """
    Build the final SpendDNA report.
    """

    report = {

        "executive_summary":
            prepare_executive_summary(
                merchant_data,
                anomaly_data,
                archetype_data,
                time_data
            ),

        "top_spending_vendors":
            prepare_top_spending_vendors(
                merchant_data
            ),

        "top_frequency_vendors":
            prepare_top_frequency_vendors(
                merchant_data
            ),

        "monthly_summary":
            prepare_monthly_summary(
                monthly_data
            ),

        "time_summary":
            prepare_time_summary(
                time_data
            ),

        "anomaly_summary":
            prepare_anomaly_summary(
                anomaly_data
            ),

        "archetype_summary":
            prepare_archetype_summary(
                archetype_data
            ),

        "metadata": {
            "Generated By": "SpendDNA",
            "Function": 9
        }
    }

    return report