import requests


def arquivo_get(url, nome_arquivo):
    arq_json = requests.get(url)
    with open(nome_arquivo, 'wb') as arq:
        arq.write(arq_json.content)
