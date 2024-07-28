import shutil
import os

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Área de Trabalho')

PASTA_INICIAL = os.path.join(DESKTOP, 'EXEMPLO')
PASTA_DESTINO = os.path.join(DESKTOP, 'NOVA_PASTA')

# Deleta toda arvore da pasta
shutil.rmtree(PASTA_DESTINO, ignore_errors=True)
# Copia toda arvore da pasta
shutil.copytree(PASTA_INICIAL, PASTA_DESTINO, dirs_exist_ok=True)
# Mover pasta
shutil.move(PASTA_DESTINO, PASTA_DESTINO+'_NOVA')
