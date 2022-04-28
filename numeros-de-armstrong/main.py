from decomposicao_numero import *

num = 0

while num < 1000000:
    if 0 <= num < 10:
        sexto_num = unidade(num)
        if (sexto_num ** 3) == num:
            print(num)
    if 10 <= num < 100:
        quinto_num = dezena(num)
        sexto_num = unidade(num)
        soma = (quinto_num[0] ** 3) + (sexto_num ** 3)
        if soma == num:
            print(num)
    if 100 <= num < 1000:
        quarto_num = centena(num)
        quinto_num = dezena(num)
        sexto_num = unidade(num)
        soma = (quarto_num[0] ** 3) + (quinto_num[0] ** 3) + (sexto_num ** 3)
        if soma == num:
            print(num)
    if 1000 <= num < 10000:
        terceiro_num = unidade_milhar(num)
        quarto_num = centena(num)
        quinto_num = dezena(num)
        sexto_num = unidade(num)
        soma = (terceiro_num[0] ** 3) + (quarto_num[0] ** 3) + (quinto_num[0] ** 3) + (sexto_num ** 3)
        if soma == num:
            print(num)
    if 10000 <= num < 100000:
        segundo_num = dezena_milhar(num)
        terceiro_num = unidade_milhar(num)
        quarto_num = centena(num)
        quinto_num = dezena(num)
        sexto_num = unidade(num)
        soma = (segundo_num[0] ** 3) + (terceiro_num[0] ** 3) + (quarto_num[0] ** 3) + (quinto_num[0] ** 3) + \
               (sexto_num ** 3)
        if soma == num:
            print(num)
    if 100000 <= num < 1000000:
        primeiro_num = centena_milhar(num)
        segundo_num = dezena_milhar(num)
        terceiro_num = unidade_milhar(num)
        quarto_num = centena(num)
        quinto_num = dezena(num)
        sexto_num = unidade(num)
        soma = (primeiro_num ** 3) + (segundo_num[0] ** 3) + (terceiro_num[0] ** 3) + (quarto_num[0] ** 3) + \
               (quinto_num[0] ** 3) + (sexto_num ** 3)
        if soma == num:
            print(num)
    num += 1
