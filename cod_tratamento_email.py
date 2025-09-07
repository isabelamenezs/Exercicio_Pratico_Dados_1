import csv
import pandas as pd
import numpy as np


dominios = ['gmail', 'outlook', 'yahoo', 'hotmail', 'uol', 'icloud', 'bol', 'ig']


def validar_email(email):
    if pd.isna(email):
        return False
    
    #garantir que o email seja um texto limpo
    email = str(email).strip()

    if email.count('@') != 1:
        return False
    
    usuario, dominio = email.split('@')
    
    if '.' not in dominio:
        return False

    # pega apenas a parte antes do primeiro ponto (ex: gmail de gmail.com.br)
    raiz = dominio.split('.')[0]

    return raiz in dominios

def tratar_emails(df):
    df['email_valido'] = df['E-mail'].apply(validar_email)
    return df

# Esse bloco só roda se você executar o arquivo direto (python valida_email.py)
if __name__ == "__main__":
    df = pd.read_csv("ex_pratico_1_dados/TnFLPByjQDmdogWPtTxJ_base_clientes_megamart.csv")
    df = tratar_emails(df)