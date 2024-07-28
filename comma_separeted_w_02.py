from os import path
import csv

CAMINHO_CSV = path.join(path.dirname(__file__), 'comma_separeted.csv')

lista_clientes = [
    {'nome': 'kaiky', 'endereço': 'rua 2'},
    {'nome': 'paula', 'endereço': 'rua 89'},
    {'nome': 'carlos', 'endereço': 'rua 700'}
]

# Abrindo o arquivo para escrita com newline='' para evitar problemas de
# quebras de linha
with open(CAMINHO_CSV, 'w', newline='', encoding='utf-8') as arquivo_csv:
    colunas = lista_clientes[0].keys()

    escritor = csv.DictWriter(
        arquivo_csv,  # Arquivo que será escrito
        fieldnames=colunas  # Nome dos cabaçalhos
    )

    escritor.writeheader()  # Definindo o nome dos cabeçalhos

    for cliente in lista_clientes:
        escritor.writerow(cliente)
