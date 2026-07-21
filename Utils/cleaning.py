import pandas as pd


def clean_dates(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize the Date column.
    """

    dataframe["Date"] = pd.to_datetime(
        dataframe["Date"],
        format="mixed",
        dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    return dataframe


def clean_transaction_type(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize transaction types.
    """

    mapping = {
        "DR": "Debit",
        "CR": "Credit",
        "Debit": "Debit",
        "Credit": "Credit"
    }

    dataframe["Type"] = (
        dataframe["Type"]
        .str.strip()
        .replace(mapping)
    )

    return dataframe


def clean_amount(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Clean amount values.
    """

    dataframe["Amount"] = (
        dataframe["Amount"]
        .str.replace("₹", "", regex=False)
        .str.replace("Rs.", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
        .astype(float)
    )

    return dataframe


def clean_text_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Clean text columns.
    """

    columns = [
        "Description",
        "Mode",
        "Ref",
        "Time"
    ]

    for column in columns:
        dataframe[column] = dataframe[column].str.strip()

    return dataframe


def clean_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Execute complete data cleaning.
    """

    dataframe = dataframe.copy()

    dataframe = clean_dates(dataframe)
    dataframe = clean_transaction_type(dataframe)
    dataframe = clean_amount(dataframe)
    dataframe = clean_text_columns(dataframe)

    dataframe = dataframe.drop_duplicates().reset_index(drop=True)

    return dataframe