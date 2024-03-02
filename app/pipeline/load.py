"""Criando modulo para carregar arquivos."""

import os

import pandas as pd


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Receber um data frame e salvar como um excel.

    args:
    data_fame (dataframe): dataframe a ser salvo
    output_path (str): caminho do arquivo a ser salvo
    file_name (str): nome do arquivo
    """
    os.makedirs(output_path, exist_ok=True)
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo Salvo com Sucesso"
