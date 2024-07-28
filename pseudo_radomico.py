# Nenhum desses numeros é verdadeiramente aleatorio,
# apenas simulam uma aleatoriedade
import random

# Define a seed do codigo, logo toda aleatoriedade será baseada nela
# Caso fique vazio, a aleatoriedade sera baseada nos microssegundos,
# assim tendo sempre alteração da aleatoridade
# random.seed(2)

# Gera um numero entre 10 e 20, pulando de dois em dois (12, 14, 16, ...)
print(random.randrange(10, 20, 2))

# Gera um numero inteiro entre 10 e 20, recomendando caso não vá usar step
print(random.randint(10, 20))

# Gera um numero de ponto flutuante entre 10 e 20
print(random.uniform(10, 20))

lista = ['maria', 'debora', 'claudia', 'felipe', 'matheus']

# Embaralha a lista original
random.shuffle(lista)
print(lista)

# Cria uma nova lista com dois nomes "aleatorios" da lista original
# k é a quantidade de itens na nova lista
nova_lista = random.sample(lista, k=2)
print(nova_lista)
