from pathlib import Path

caminho = Path()

# Retorna o caminho absoluto até o diretorio do projeto
print(caminho.absolute())

# Retorna o caminho até o arquivo
caminho = Path(__file__)
print(caminho)

# Retorna o caminho do diretorio do arquivo main
print(caminho.parent)
print(caminho.parent.parent)
# A cada .parent, irá retornando uma pasta acima
print(caminho.parent.parent.parent)

# Retorna a home do sistema
print(Path.home())

# Criando um novo caminho
CAMINHO_ARQUIVO = caminho.parent / 'arquivo.txt'
print(CAMINHO_ARQUIVO)

# Cria o arquivo descrito
CAMINHO_ARQUIVO.touch()
# Deleta o arquivo descrito
CAMINHO_ARQUIVO.unlink()

# Escrevendo em um arquivo criado
CAMINHO_ARQUIVO = caminho.parent / 'arquivo02.txt'
CAMINHO_ARQUIVO.write_text('Ola mundo')
# Lendo oque foi escrito
print(CAMINHO_ARQUIVO.read_text())


PASTA = caminho.parent / 'nova pasta'
# Criando um novo diretorio, caso ele já exista, não cria nada, nem retorna
# erro
PASTA.mkdir(exist_ok=True)

NOVO_ARQUIVO = PASTA / 'arquivo.txt'
NOVO_ARQUIVO.touch()
