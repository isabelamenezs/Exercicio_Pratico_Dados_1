import pandas as pd
import numpy as np


#Coloquei para que toda coluna seja valores numéricos

def trata_valor(df):
    df["Valor Compra"] = pd.to_numeric(df["Valor Compra"], errors="coerce")
    return df

#so serve para exibir no colab ou no jupyter, vou alterar no sheets para moeda
#df.style.format({"Valor Compra": "R$ {:,.2f}".format})

if __name__ == "__main__":
    df = pd.read_csv("ex_pratico_1_dados/TnFLPByjQDmdogWPtTxJ_base_clientes_megamart.csv")
    df = trata_valor(df)
