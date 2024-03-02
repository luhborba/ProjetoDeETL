"""Modulo para transformar dados."""
from typing import List

import pandas as pd


def concatenar_df(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatenates a list of pandas DataFrames into a single DataFrame with the option to ignore the original index and create a new one.

    Args:
        dataframes (List[pd.DataFrame]): The list of DataFrames to be concatenated.

    Returns:
        pd.DataFrame: The concatenated DataFrame.
    """
    return pd.concat(dataframes, ignore_index=True)
