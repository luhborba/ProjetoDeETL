import os # biblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos
import pandas as pd
from typing import List

"""
Função para ler arquivos de uma pasta data/input e retornar uma lista de dataframes.

args: input_path (str): caminho da pasta com os arquivos

return: lista de dataframes
"""
path = "data/input"

def extranindo_dados_excel(path: str) -> List[pd.DataFrame]:
    arquivos = glob.glob(os.path.join(path, "*.xlsx"))

    lista_df = []

    for arquivo in arquivos:
        lista_df.append(pd.read_excel(arquivo))
    
    return lista_df 

if __name__ == "__main__":
    lista = extranindo_dados_excel(path)
    print(lista)
