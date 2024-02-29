import pandas as pd
from app.pipeline.trasform import concatenar_df

df_1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df_2 = pd.DataFrame({"a": [7, 8, 9], "b": [10, 11, 12]})

def testar_a_concatenacao_df():
    
    # Gerando Lista de dataframes para teste
    df_list =  [df_1,df_2]
    # Concatenando os dataframes para realização de testes
    data_frame= pd.concat(df_list, ignore_index=True)
    
    # Chamando função criada no transform
    df = concatenar_df(df_list)
    
    assert df.shape == (6, 2) # Testando se o dataframe foi concatenado corretamente através do shape
    assert data_frame.equals(df) # Testando se os dataframes são igual, tanto no pd.concat quanto na função criada