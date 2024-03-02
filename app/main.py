from pipeline.extract import extranindo_dados_excel
from pipeline.load import load_excel
from pipeline.trasform import concatenar_df

if __name__ == '__main__':
    path = 'data/input'
    lista_df = extranindo_dados_excel(path)
    df = concatenar_df(lista_df)
    load_excel(df, 'data/output', 'output')
