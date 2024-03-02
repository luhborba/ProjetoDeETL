import os # biblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos
import pandas as pd
from typing import List




def extranindo_dados_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler arquivos de uma pasta data/input e retornar uma lista de dataframes.

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    arquivos = glob.glob(os.path.join(path, "*.xlsx"))

    lista_df = []

    for arquivo in arquivos:
        lista_df.append(pd.read_excel(arquivo))
    
    return lista_df 

if __name__ == "__main__":
    path = "data/input"
    lista = extranindo_dados_excel(path)
    print(lista)
