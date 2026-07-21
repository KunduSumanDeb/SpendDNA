"""
Display helper functions.
"""

import pandas as pd


def show_shape(dataframe: pd.DataFrame) -> None:
    """
    Display dataframe dimensions.
    """

    print(f"Rows    : {dataframe.shape[0]}")
    print(f"Columns : {dataframe.shape[1]}")


def show_columns(dataframe: pd.DataFrame) -> None:
    """
    Display dataframe columns.
    """

    for index, column in enumerate(dataframe.columns, start=1):
        print(f"{index}. {column}")