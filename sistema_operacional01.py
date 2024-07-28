import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Área de Trabalho')

PASTA_INICIAL = os.path.join(DESKTOP, 'EXEMPLO')
PASTA_DESTINO = os.path.join(DESKTOP, 'NOVA_PASTA')

# Cria a pasta no destino caso ela não exista
# os.makedirs(PASTA_DESTINO, exist_ok=True)


for root, dirs, files in os.walk(PASTA_INICIAL):
    for dir_ in dirs:
        caminho_final = os.path.join(PASTA_DESTINO, dir_)
        os.makedirs(caminho_final)
    for file in files:
        caminho_original = os.path.join(root, file)
        caminho_destino = caminho_original.replace(
            PASTA_INICIAL, PASTA_DESTINO)
        shutil.copy(caminho_original, caminho_destino)
