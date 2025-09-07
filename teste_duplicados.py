import pandas as pd

def tratar_duplicados(df):
    """
    Cria uma coluna 'Duplicado' que marca True para todas
    as ocorrências de linhas duplicadas no DataFrame.
    """
    df["registros_duplicados"] = df.duplicated(keep=False)
    return df