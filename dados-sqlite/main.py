import sqlite3
from arquivo_get import *
from load_dados import *


url_arq = 'https://dadosabertos.aneel.gov.br/dataset/dbe863ff-f27f-49bf-ad07-84eddb1629ba/resource' \
          '/a3dfbad2-4fc2-478b-b13a-bbf6a4269c84/download/projetoretornoinvestimento.json'
arquivo_get(url_arq, 'arquivo.json')

tabela = load_dados('arquivo.json')

conn = sqlite3.connect('Python_Project.db')

tabela.to_sql(name='ProjetoRetornoInvestimento', con=conn, if_exists='append', index=False)

conn.close()
