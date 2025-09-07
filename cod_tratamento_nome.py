
import pandas as pd
import numpy as np


expressoes = ['sr.', 'sra.', 'srta.', 'dr.', 'dra.']

#Coloquei todos os nomes encontrados em letra minuscula para padronizar e fazer a limpeza
def nome_minusculo(nome):
    return str(nome).lower()

#método para a retirada dos titulos extras
def limpar_titulo(nome):
    for e in expressoes:
        nome = nome.replace(e, "")
    return nome.strip()

def tratar_nome(df):
    df["Nome Completo"] = df["Nome Completo"].apply(nome_minusculo)
    df["Nome Completo"] = df["Nome Completo"].apply(limpar_titulo)
    #Método utilizado para deixar as primeiras letras de cada nome maiusculas
    df['Nome Completo'] = df['Nome Completo'].str.title()
    return df

