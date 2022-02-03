import pandas as pd


def mostrar_dados(base):

    colunas = ['CO_POSICAO', 'SG_AREA','CO_ITEM', 'TX_GABARITO',
               'CO_HABILIDADE', 'TX_COR','CO_PROVA', 'TP_LINGUA', 'IN_ITEM_ADAPTADO']

    dados = pd.DataFrame(base, columns=colunas)
    print()
    print(dados.head())
    print(informacoes(dados))


def informacoes(base):
    print()
    print(base.info())
