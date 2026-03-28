""" Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:
Crie uma pasta chamada extraido/.
Extraia o conteúdo do .zip dentro da pasta criada.
Ao final, liste todos os arquivos extraídos. """
import shutil
from pathlib import Path

#CRIANDO PASTA
pasta=Path("EXERCICIOSzzz/EXTRAIDO")
pasta.mkdir(exist_ok=True, parents=True)

#EXTRAINDO ARQUIVO
X=Path("EXERCICIOSzzz/")
for arquivo in X.glob("*.zip"):
    shutil.unpack_archive(arquivo, pasta)

#PRINTANDO
for i, arquivo in enumerate(pasta.iterdir(), start=1):
    print (f"{i}-{arquivo.name}")