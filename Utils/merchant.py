"""
merchant.py

Merchant Insights Utility

This module generates merchant-level analytics from the vendor-normalized
transaction dataset.

Responsibilities
----------------
- Validate required columns
- Filter merchant spending transactions
- Compute merchant statistics
- Identify primary merchant categories
- Generate monthly merchant summaries
- Rank merchants by spending and frequency
- Create merchant metadata
- Export merchant insights
"""

import pandas as pd


# ============================================================
# REQUIRED COLUMNS
# ============================================================

REQUIRED_COLUMNS = [
    "Date",
    "Amount",
    "Transaction Type",
    "Category",
    "Vendor",
]
    
def validate_columns(df):
    """
    Validate that all required columns are present.

    Parameters
    ----------
    df : pandas.DataFrame
        Input transaction dataframe.

    Raises
    ------
    ValueError
        If one or more required columns are missing.
    """
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )
    
def prepare_spending_data(df):
    """
    Prepare transaction data for merchant analysis.

    Filters only debit transactions and removes rows with
    missing vendor names.

    Parameters
    ----------
    df : pandas.DataFrame
        Input transaction dataframe.

    Returns
    -------
    pandas.DataFrame
        Clean dataframe containing merchant spending data.
    """

    spending_df = df.copy()

    # Keep only debit transactions
    spending_df = spending_df[
        spending_df["Transaction Type"].str.upper() == "DEBIT"
    ]

    # Remove rows with missing vendors
    spending_df = spending_df.dropna(subset=["Vendor"])

    # Remove UNKNOWN vendors
    spending_df = spending_df[
        spending_df["Vendor"] != "UNKNOWN"
    ]

    return spending_df.reset_index(drop=True)

def merchant_statistics(df):
    """
    Compute merchant-level spending statistics.

    Parameters
    ----------
    df : pandas.DataFrame
        Merchant spending dataframe.

    Returns
    -------
    pandas.DataFrame
        Summary statistics for each merchant.
    """

    summary = (
        df.groupby("Vendor")
        .agg(
            Transactions=("Vendor", "count"),
            Total_Spend=("Amount", "sum"),
            Average_Spend=("Amount", "mean"),
            Maximum_Spend=("Amount", "max"),
            Minimum_Spend=("Amount", "min"),
        )
        .reset_index()
    )

    summary["Average_Spend"] = summary["Average_Spend"].round(2)
    summary = summary.sort_values(
        by="Total_Spend",
        ascending=False
    ).reset_index(drop=True)

    return summary

def merchant_category_profile(df):
    """
    Determine the dominant spending category for each merchant.

    Parameters
    ----------
    df : pandas.DataFrame
        Merchant spending dataframe.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing each merchant and its primary category.
    """

    category_counts = (
        df.groupby(["Vendor", "Category"])
        .size()
        .reset_index(name="Transaction_Count")
    )

    dominant_category = (
        category_counts
        .sort_values(
            by=["Vendor", "Transaction_Count"],
            ascending=[True, False]
        )
        .drop_duplicates(subset="Vendor")
        .loc[:, ["Vendor", "Category"]]
        .rename(columns={"Category": "Primary_Category"})
        .reset_index(drop=True)
    )

    return dominant_category

def merchant_monthly_summary(df):
    """
    Compute monthly spending summary for each merchant.

    Parameters
    ----------
    df : pandas.DataFrame
        Merchant spending dataframe.

    Returns
    -------
    pandas.DataFrame
        Monthly spending by merchant.
    """

    monthly_df = df.copy()

    monthly_df["Month"] = monthly_df["Date"].dt.to_period("M").astype(str)

    summary = (
        monthly_df.groupby(["Vendor", "Month"])
        .agg(
            Total_Spend=("Amount", "sum"),
            Transactions=("Amount", "count")
        )
        .reset_index()
        .sort_values(["Vendor", "Month"])
        .reset_index(drop=True)
    )

    return summary

def top_merchants_by_spend(summary_df, top_n=10):
    """
    Return the top merchants ranked by total spending.

    Parameters
    ----------
    summary_df : pandas.DataFrame
        Merchant summary dataframe.

    top_n : int, default=10
        Number of merchants to return.

    Returns
    -------
    pandas.DataFrame
    """

    return (
        summary_df
        .sort_values(
            by="Total_Spend",
            ascending=False
        )
        .head(top_n)
        .reset_index(drop=True)
    )

def top_merchants_by_frequency(summary_df, top_n=10):
    """
    Return the most frequently used merchants.

    Parameters
    ----------
    summary_df : pandas.DataFrame
        Merchant summary dataframe.

    top_n : int, default=10
        Number of merchants to return.

    Returns
    -------
    pandas.DataFrame
    """

    return (
        summary_df
        .sort_values(
            by="Transactions",
            ascending=False
        )
        .head(top_n)
        .reset_index(drop=True)
    )

def merchant_metadata(summary_df):
    """
    Generate merchant-level metadata.

    Parameters
    ----------
    summary_df : pandas.DataFrame

    Returns
    -------
    dict
    """

    metadata = {
        "total_merchants": int(summary_df["Vendor"].nunique()),
        "total_transactions": int(summary_df["Transactions"].sum()),
        "total_spend": float(summary_df["Total_Spend"].sum()),
        "average_transaction": round(
            summary_df["Average_Spend"].mean(),
            2
        ),
        "largest_merchant": summary_df.iloc[0]["Vendor"],
        "most_frequent_merchant": (
            summary_df.sort_values(
                by="Transactions",
                ascending=False
            )
            .iloc[0]["Vendor"]
        ),
    }

    return metadata

def generate_merchant_insights(df):
    """
    Execute the complete merchant insights pipeline.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
    """

    validate_columns(df)

    spending_df = prepare_spending_data(df)

    summary_df = merchant_statistics(spending_df)

    category_df = merchant_category_profile(spending_df)

    monthly_df = merchant_monthly_summary(spending_df)

    summary_df = summary_df.merge(
        category_df,
        on="Vendor",
        how="left"
    )

    top_spend_df = top_merchants_by_spend(summary_df)

    top_frequency_df = top_merchants_by_frequency(summary_df)

    metadata = merchant_metadata(summary_df)

    return {
        "merchant_summary": summary_df,
        "merchant_category": category_df,
        "monthly_summary": monthly_df,
        "top_spend": top_spend_df,
        "top_frequency": top_frequency_df,
        "metadata": metadata,
    }