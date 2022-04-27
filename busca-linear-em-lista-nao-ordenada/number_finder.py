print("********************* OLÁ! BEM VINDO ***********************")
num_procurado = (input("Qual numero deseja encontrar na lista? "))
with open("numeros_aleatorios.txt", "r", encoding="utf-8") as arquivo:
    lista = []
    lista_limpa = []
    for linha in arquivo.readlines():
        lista.append(linha.split())
    for i in lista:
        lista_limpa.extend(i)

    cont = 0
    for x in range(0, len(lista_limpa)):
        if lista_limpa[x] == num_procurado:
            print(f'{num_procurado} encontrado no indice {x} da lista')
            cont += 1

    if cont == 0:
        print(-1)
