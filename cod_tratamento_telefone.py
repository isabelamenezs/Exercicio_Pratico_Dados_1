import pandas as pd
import numpy as np

df = pd.read_csv("ex_pratico_1_dados/TnFLPByjQDmdogWPtTxJ_base_clientes_megamart.csv")

df['Telefone'] = df['Telefone'].astype(str)

ddds_validos = [str(i) for i in range(11, 100)]
numeros_servico = ['0800', '0900', '0300', '4004', '700', '4517']

# Função para limpar e padronizar
def limpar_telefone(tel):
    if pd.isna(tel):
        return False
    
    #manter apenas números
    tel = ''.join(filter(str.isdigit, tel))

    # remover o código do país '55' se estiver no início
    if tel.startswith('55'):
        tel = tel[2:]

    if any(tel.startswith(ns) for ns in numeros_servico):
        return False
    
    #eliminar o zero a esquerda na frente do ddd
    if tel.startswith('0') and len(tel) >= 11:
        tel = tel[1:]

    # precisa ter pelo menos 10 dígitos (DDD + número)
    if len(tel) < 10:
        return False
    ddd = tel[:2]
    return ddd in ddds_validos

def padronizar_telefone(tel):
    if pd.isna(tel):
        return 'nan'

    # manter apenas dígitos
    tel_limpo = ''.join(filter(str.isdigit, str(tel)))
    
    # identificar números de serviço
    numeros_servico = ['0800', '0900', '0300', '4004', '700', '4517']
    if any(tel_limpo.startswith(ns) for ns in numeros_servico):
        return f"[INVÁLIDO] {tel_limpo}"
    
    # remover código do país '55'
    if tel_limpo.startswith('55'):
        tel_limpo = tel_limpo[2:]
    
    # remover zero à esquerda do DDD
    if tel_limpo.startswith('0') and len(tel_limpo) >= 11:
        tel_limpo = tel_limpo[1:]


    # validar comprimento mínimo
    if len(tel_limpo) < 10:
        return f"[INVÁLIDO] {tel_limpo}"

    ddd = tel_limpo[:2]
    numero = tel_limpo[2:]

    # fixo com 8 dígitos
    if len(numero) == 8:
        return f"({ddd}) {numero[:4]}-{numero[4:]}"
    else:
        # números que não se encaixam nos padrões
        return f"[OUTRO] {tel_limpo}"

def tratar_telefone(df):
    df['Telefone_valido'] = df['Telefone'].apply(limpar_telefone)
    df['Telefone'] = df['Telefone'].apply(padronizar_telefone)
    return df

if __name__ == "__main__":
    df = pd.read_csv("ex_pratico_1_dados/TnFLPByjQDmdogWPtTxJ_base_clientes_megamart.csv")
    df = tratar_telefone(df)