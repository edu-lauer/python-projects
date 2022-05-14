import pandas as pd


def load_dados(nome_arquivo):
    df = pd.read_json(nome_arquivo)
    return df
