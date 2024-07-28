from datetime import datetime
import locale
import string
from os import path


# O locale.LC_ALL define que a configuração regional informada na string será
# usada para todas as categorias desde dinheiro até datas. Como a string está
# vazia '', irá se basear na região que o sistema esta configurada
locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(valor: float) -> str:
    brl = locale.currency(
        val=valor,  # Indica o valor a ser convertido
        symbol='R$',  # Indica que o símbolo da moeda
        grouping=True  # Indica que você deseja usar o agrupamento de milhares
    )
    return brl


data = datetime(2024, 7, 27)

dados = dict(
    nome='joão',
    valor=converte_para_brl(12_643_546),
    data=data.strftime('%d/%m/%Y'),
    empresa='IBM',
    telefone='+55 (11) 98765-4321'
)

CAMINHO_TEXTO = path.join(path.dirname(__file__), 'texto_template.txt')

with open(CAMINHO_TEXTO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

CAMINHO_TEXTO = CAMINHO_TEXTO.replace(
    'texto_template.txt', 'texto_template_feito.txt')

template = string.Template(texto)

with open(CAMINHO_TEXTO, 'w', encoding='utf-8') as arquivo:
    arquivo.write(template.substitute(dados))

print('E-mail preparado!')


# Assim podemos mudar o indicador do template do texto
class MyTemplate(string.Template):
    delimiter = '%'
