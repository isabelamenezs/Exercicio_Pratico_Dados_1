
import pandas as pd
import numpy as np
from datetime import datetime


#padronizando todas as datas para o tipo de objeto datetime
def tratar_datas(df):
    hoje = pd.Timestamp(datetime.today().date())

    # converte só para validação, não altera a coluna original
    datas_nascimento = pd.to_datetime(df['Data Nascimento'], format="%d/%m/%Y", errors='coerce')
    datas_ultima = pd.to_datetime(df['Última Compra'], errors='coerce')

    # valida se as datas são válidas e <= hoje
    df['data_nascimento_valida'] = datas_nascimento.notna() & (datas_nascimento <= hoje)
    df['ultima_compra_valida'] = datas_ultima.notna() & (datas_ultima <= hoje)

    return df

    #print(df[['Data Nascimento', 'Última Compra']])