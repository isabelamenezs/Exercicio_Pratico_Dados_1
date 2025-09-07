import csv
import pandas as pd
import numpy as np

#print(df.head())
#print(df.columns)

#Serve para ver a quantidade de colunas com linhas vazias
#print(df.isnull().sum())

#Padronizando os cpfs para se transformarem somente em conjunto de digitos sem "-" e "."
#df['CPF'] = df['CPF'].astype(str)
#df['CPF'] = df['CPF'].str.replace('.', '')
#df['CPF'] = df['CPF'].str.replace('-', '')
#print(df['CPF'])

#validação do cpf
def validar_cpf(cpf):
  if pd.isna(cpf):
    return False
  return len(cpf) == 11 and cpf.isdigit()

def tratar_cpf(df):
  df['CPF'] = df['CPF'].astype(str)
  df['CPF'] = df['CPF'].str.replace('.', '')
  df['CPF'] = df['CPF'].str.replace('-', '')
  df['cpf_valido'] = df['CPF'].apply(validar_cpf)
  return df
  #print(df['cpf_valido'].sum())

