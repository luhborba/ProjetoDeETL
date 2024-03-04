"""Modulo para transformar dados."""

from typing import List

import pandas as pd


def concatenar_df(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """
   Concatena a lista de Dataframes e retorna um dataframe unico.

    Args:
        dataframes (List[pd.DataFrame]): The list of DataFrames to be concatenated.

    Returns:
        pd.DataFrame: The concatenated DataFrame.
    """
    return pd.concat(dataframes, ignore_index=True)
