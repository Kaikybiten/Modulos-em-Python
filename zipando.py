# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'zip_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'zip_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'zip_descompactado'

# Removendo arquivos caso eles já existam
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for _root, _dirs, _files in os.walk(CAMINHO_ZIP_DIR):
        for _file in _files:
            zip.write(os.path.join(_root, _file),  # Local que será escrito
                      _file  # Oque será escrito
                      )
