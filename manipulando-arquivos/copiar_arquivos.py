import os
import shutil


def copiar_arquivos(pasta_origem, pasta_destino):
    for root, dirs, files in os.walk(pasta_origem):
        for file in files:
            path_origem = root + '/' + file
            path_destino = pasta_destino + '/' + file
            shutil.copyfile(path_origem, path_destino)
