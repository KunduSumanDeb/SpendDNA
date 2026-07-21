"""
Input and output helper functions.
"""

from pathlib import Path
import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file.
    """
    return pd.read_csv(path)


def load_pickle(path: Path) -> pd.DataFrame:
    """
    Load a pickle file.
    """
    return pd.read_pickle(path)


def save_pickle(dataframe: pd.DataFrame, path: Path) -> None:
    """
    Save a dataframe as a pickle file.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_pickle(path)