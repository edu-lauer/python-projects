def get_contatos(arquivo):
    nomes = []
    emails = []
    with open(arquivo, mode="r", encoding="utf-8") as arq:
        for linha in arq:
            nomes.append(linha.split()[0])
            emails.append(linha.split()[1])

        return nomes, emails
    