import random


def busca(lista_valores, limite_esquerda, limite_direita, valor):  # função que realiza a busca pelo valor na lista
    indice_meio = (limite_esquerda + limite_direita) // 2
    valor_meio = lista_valores[indice_meio]
    if limite_direita < limite_esquerda:
        return -1
    if valor_meio == valor:
        return indice_meio
    elif valor > valor_meio:
        return busca(lista_valores, indice_meio + 1, len(lista_valores) - 1, valor)
    else:
        return busca(lista_valores, limite_esquerda, indice_meio - 1, valor)


lista = []
for x in range(0, 101):  # loop que vai gerar a lista de 100 numeros aleatórios entre 0 e 1000
    lista.append(random.randint(0, 1001))

lista.sort()  # ordena a lista em números crescentes
print(lista)
num_procurado = int(input("Digite o numero a ser procurado: "))  # usuário entra com o número a ser procurado
direta = len(lista) - 1
indice_num = busca(lista, 0, direta, num_procurado)  # chamada da função que vai buscar o número

if indice_num != -1:
    print(f'{num_procurado} encontrado no indice {indice_num}')
else:
    print(indice_num)
