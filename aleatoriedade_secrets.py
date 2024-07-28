# O modulo secrets utiliza funções do sistema operacional para gerar números
# aleatórios. Estas funções são projetadas para serem seguras e imprevisíveis
import secrets

# Gera um numero aleatorio abaixo de 100
print(secrets.randbelow(100))

# Escolhe um numero dentro da lista
print(secrets.choice[10, 20, 30])

# Podemos criar uma instancia e apartir de agora ela randomiza de uma forma
# mais segura, garantindo a imprevisibilidade dos numeros gerados
random = secrets.SystemRandom()

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
