from copiar_arquivos import *
from criar_arquivos import *
from move_arquivos import *
from renomear_arquivos import *
from zipar_arquivo import *


pasta_arquivos_origem = r'/home/elauer/Desktop/Python-projects/manipulando-arquivos/arquivos'
pasta_arquivos_destino = r'/home/elauer/Desktop/Python-projects/manipulando-arquivos/bkp'

criar_arquivos(5, 3)
lista_arquivos = [arq for arq in os.listdir() if arq.lower().endswith(".txt")]

move_arquivos(lista_arquivos, '', './arquivos')

copiar_arquivos(pasta_arquivos_origem, pasta_arquivos_destino)

renomear_arquivos(pasta_arquivos_origem, 3)

zipar_arquivo(pasta_arquivos_destino, "arquivos")
