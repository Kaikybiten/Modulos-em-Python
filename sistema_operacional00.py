import os

# Enviando comandos para o prompt
os.system('cls')
print('a' * 800)
os.system('dir')
print()


# Caminho de arquivos
caminho = os.path.join('desktop', 'cursos', 'arquivo.txt')
print(caminho)

diretorio, arquivo = os.path.split(caminho)
print(diretorio)
print(arquivo)

nome_arquivo, arquivo_extencao = os.path.splitext(arquivo)
print(nome_arquivo)
print(arquivo_extencao)

print(os.path.exists(caminho))  # Verifica existencia do caminho
print(os.path.abspath('.'))  # Retona o caminho da parta atual
print(os.path.basename(caminho))  # Retorna a parte final
print(os.path.dirname(caminho))  # Retorna o diretorio
print()


caminho_diretorio = os.path.join('/Users', 'kaiky', 'OneDrive',
                                 'Área de Trabalho', 'Programação', 'Cursos',
                                 'Udemy - Python')

for pasta in os.listdir(caminho_diretorio):
    caminho_pasta = f'{caminho_diretorio}\\{pasta}'
    if not (os.path.isdir(caminho_pasta)):  # Verificando se é pasta
        continue

    print(pasta)
    for arquivo in os.listdir(caminho_pasta):
        print('>', arquivo)
print()


for paths, dirs, files in os.walk('C:\\Users\\kaiky\\OneDrive\\Área de '
                                  'Trabalho\\Trabalhos\\game maker treino'):
    print(paths)
    for dir_ in dirs:
        print('  ', dir_)
    for file_ in files:
        print('  ', file_)
