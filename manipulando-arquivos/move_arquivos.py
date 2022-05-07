import shutil


def move_arquivos(lista_de_arquivos, source, destino):  # destino = "./arquivos"
    for arq in lista_de_arquivos:
        shutil.move(f'.{source}/{arq}', f'{destino}')
