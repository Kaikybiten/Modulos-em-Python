import string
import secrets

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


#       Gerando senha

# Criando uma instancia que tem função de randomizar
randomizador = secrets.SystemRandom()
# Adicionando todos os caracteres possiveis em uma string
caracteres = string.ascii_letters + string.digits
# Colocando 8 caracteres aleatorios em uma lista
senha = randomizador.choices(caracteres, k=12)
senha_final = ''.join(senha)
print(senha_final)
