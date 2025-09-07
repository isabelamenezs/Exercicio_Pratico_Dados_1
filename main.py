import pandas as pd
from cod_tratamento_cpf import tratar_cpf
from cod_tratamento_data import tratar_datas
from cod_tratamento_email import tratar_emails
from cod_tratamento_estado import tratar_estado
from cod_tratamento_nome import tratar_nome
from cod_tratamento_telefone import tratar_telefone
from cod_tratamento_valor import trata_valor
from teste_duplicados import tratar_duplicados

if __name__ == "__main__":
    df = pd.read_csv("ex_pratico_1_dados/TnFLPByjQDmdogWPtTxJ_base_clientes_megamart.csv")
    # aplica o tratamento
    df = tratar_duplicados(df)
    df = tratar_emails(df)
    df = trata_valor(df)
    df = tratar_telefone(df)
    df = tratar_estado(df)
    df = tratar_nome(df)
    df = tratar_cpf(df)
    df = tratar_datas(df)


    # salva o resultado
    df.to_csv("ex_pratico_1_dados/dados_tratados.csv", index=False, sep = ";", decimal = ",")
    print("Novo CSV gerado com sucesso!")