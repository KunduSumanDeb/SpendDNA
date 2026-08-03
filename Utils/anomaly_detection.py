import pandas as pd
import numpy as np
ANOMALY_THRESHOLD = 2.0
def prepare_category_statistics(df):
    """
    Compute spending statistics for each category.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Category-wise mean, standard deviation,
        transaction count and total spend.
    """

    required_columns = {
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data = data[
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    ]

    statistics = (
        data.groupby("Category")["Amount"]
        .agg(
            Mean="mean",
            Std="std",
            Count="count",
            Total="sum"
        )
        .reset_index()
    )

    statistics["Std"] = (
        statistics["Std"]
        .fillna(0.0)
    )

    return statistics

def calculate_z_scores(df, statistics):
    """
    Calculate z-score for debit transactions.

    Parameters
    ----------
    df : pandas.DataFrame
    statistics : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Transaction data with z-score.
    """

    data = df.copy()

    data = data.merge(
        statistics,
        on="Category",
        how="left"
    )

    data["Z_Score"] = np.nan

    debit_mask = (
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    )

    valid_mask = debit_mask & (data["Std"] > 0)

    data.loc[valid_mask, "Z_Score"] = (
        (
            data.loc[valid_mask, "Amount"]
            - data.loc[valid_mask, "Mean"]
        )
        / data.loc[valid_mask, "Std"]
    )

    return data

def detect_anomalies(df):
    """
    Detect anomalous transactions using z-score.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Transactions having z-score greater than
        the anomaly threshold.
    """

    if "Z_Score" not in df.columns:
        raise ValueError(
            "Z_Score column not found."
        )

    anomalies = (
        df[df["Z_Score"] > ANOMALY_THRESHOLD]
        .copy()
    )

    anomalies = anomalies.sort_values(
        by="Z_Score",
        ascending=False
    )

    anomalies = anomalies.reset_index(
        drop=True
    )

    anomalies = (
        df[
            (df["Transaction Type"].str.upper() == "DEBIT") &
            (df["Z_Score"] > ANOMALY_THRESHOLD)
        ]
        .copy()
    )

    return anomalies

def detect_anomalies(df):
    """
    Detect anomalous transactions using z-score.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Transactions with z-score above threshold.
    """

    if "Z_Score" not in df.columns:
        raise ValueError(
            "Z_Score column not found."
        )

    anomalies = (
        df[df["Z_Score"] > ANOMALY_THRESHOLD]
        .copy()
    )

    anomalies = anomalies.sort_values(
        by="Z_Score",
        ascending=False
    )

    anomalies = anomalies.reset_index(
        drop=True
    )

    return anomalies

def get_top_anomalies(anomalies, top_n=5):
    """
    Return the highest scoring anomalies.

    Parameters
    ----------
    anomalies : pandas.DataFrame
    top_n : int

    Returns
    -------
    pandas.DataFrame
        Top anomalous transactions.
    """

    return (
        anomalies
        .head(top_n)
        .reset_index(drop=True)
    )

def prepare_metadata(transactions, anomalies):
    """
    Prepare metadata for anomaly detection.

    Parameters
    ----------
    transactions : pandas.DataFrame
    anomalies : pandas.DataFrame

    Returns
    -------
    dict
        Metadata summary.
    """

    metadata = {
        "total_transactions": len(transactions),
        "total_anomalies": len(anomalies),
        "anomaly_threshold": ANOMALY_THRESHOLD,
        "categories": transactions["Category"].nunique()
    }

    return metadata

def generate_anomaly_detection(df):
    """
    Generate complete anomaly detection analysis.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
        Complete anomaly detection results.
    """

    category_statistics = prepare_category_statistics(df)

    transactions_with_zscore = calculate_z_scores(
        df,
        category_statistics
    )

    anomalies = detect_anomalies(
        transactions_with_zscore
    )

    top_anomalies = get_top_anomalies(
        anomalies
    )

    metadata = prepare_metadata(
        df,
        anomalies
    )

    return {
        "category_statistics": category_statistics,
        "transactions_with_zscore": transactions_with_zscore,
        "anomalies": anomalies,
        "top_anomalies": top_anomalies,
        "metadata": metadata
    }