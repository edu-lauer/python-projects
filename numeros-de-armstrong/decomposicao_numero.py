def centena_milhar(numero):
    casa_centena_milhar = int(numero / 100000)
    return casa_centena_milhar


def dezena_milhar(numero):
    casa_centena_milhar = centena_milhar(numero)
    numero_sem_centena_milhar = numero - (casa_centena_milhar * 100000)  # retirando a centena de milhar do número
    casa_dezena_milhar = int(numero_sem_centena_milhar / 10000)
    return casa_dezena_milhar, numero_sem_centena_milhar


def unidade_milhar(numero):
    casa_dezena_milhar, numero_sem_centena_milhar = dezena_milhar(numero)
    numero_sem_dezena_milhar = numero_sem_centena_milhar - (casa_dezena_milhar * 10000)  # retirando a dezena de milhar
    casa_unidade_milhar = int(numero_sem_dezena_milhar / 1000)
    return casa_unidade_milhar, numero_sem_dezena_milhar


def centena(numero):
    casa_unidade_milhar, numero_sem_dezena_milhar = unidade_milhar(numero)
    numero_sem_unidade_milhar = numero_sem_dezena_milhar - (casa_unidade_milhar * 1000)  # retirando a unidade de milhar
    casa_centena = int(numero_sem_unidade_milhar / 100)
    return casa_centena, numero_sem_unidade_milhar


def dezena(numero):
    casa_centena, numero_sem_unidade_milhar = centena(numero)
    numero_sem_centena = numero_sem_unidade_milhar - (casa_centena * 100)
    casa_dezena = int(numero_sem_centena / 10)
    return casa_dezena, numero_sem_centena


def unidade(numero):
    casa_dezena, numero_sem_centena = dezena(numero)
    numero_sem_dezena = numero_sem_centena - (casa_dezena * 10)
    casa_unidade = numero_sem_dezena
    return casa_unidade
