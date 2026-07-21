import pandas as pd


def validate_dataframe(dataframe: pd.DataFrame) -> dict:
    """
    Validate a dataframe and return a summary.
    """

    summary = {
        "rows": dataframe.shape[0],
        "columns": dataframe.shape[1],
        "missing_values": dataframe.isnull().sum().sum(),
        "duplicate_rows": dataframe.duplicated().sum(),
    }

    print("Validation Summary")
    print("-" * 40)

    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title():20}: {value}")

    return summary