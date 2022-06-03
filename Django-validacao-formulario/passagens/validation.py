def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'


def caractere_numerico(campo, nome_campo, lista_de_erros):
    """Verifica se existe algum caractere numérico no campo"""
    if any(char.isdigit() for char in campo):
        lista_de_erros[nome_campo] = 'inválido: não insira números'


def valida_data(data_ida, data_volta, data_pesquisa, lista_de_erros):
    """Verifica se data de ida é maior que data de volta ||
    Verifica se a data de ida é maior do que em esta realizando consulta"""
    if data_ida > data_volta:
        lista_de_erros['data_ida'] = 'Data de ida nao pode ser maior que data de volta'

    elif data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser anterior ao dia de hoje'
