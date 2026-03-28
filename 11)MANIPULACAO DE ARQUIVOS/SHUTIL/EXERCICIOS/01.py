""" Crie um script que:
Crie uma pasta imagens.
Coloque 2 arquivos fictícios .png dentro dela
Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup. """
import shutil
from pathlib import Path

##CRIANDO PASTAS
pasta=Path("EXERCÍCIOSz/IMAGENS")
pasta.mkdir(parents=True, exist_ok=True)

backup=Path("EXERCÍCIOSz/BACKUP")
backup.mkdir(parents=True, exist_ok=True)

##CRIANDO ARQUIVOS
Path("EXERCÍCIOSz/IMAGENS/Arquiivo1.png").touch(exist_ok=True)
Path("EXERCÍCIOSz/IMAGENS/Arquiivo2.png").touch(exist_ok=True)

##COPIANDO
for arquivo in pasta.glob("*.png"):
    shutil.copy(arquivo, "EXERCÍCIOSz/BACKUP")
