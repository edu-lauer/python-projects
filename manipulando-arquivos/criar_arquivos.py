import string
import random


def criar_arquivos(tamanho_nome, numero_arquivos):
    for x in range(numero_arquivos):
        nome_arquivo = ''.join(random.choice(string.ascii_letters) for _ in range(tamanho_nome))
        conteudo_arquivo = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(500))

        arquivo = open(nome_arquivo + ".txt", "a", encoding="UTF-8")

        arquivo.write(conteudo_arquivo)

        arquivo.close()
