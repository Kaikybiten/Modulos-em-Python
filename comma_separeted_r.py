import csv
from os import path

CAMINHO_CSV = path.join(path.dirname(__file__), 'comma_separeted.csv')
print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    print(next(leitor))
    print(next(leitor))
    print(next(leitor))


with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    print(next(leitor))
    print(next(leitor))

# Ambos podem ser iteirados com "for"
