""" Dentro da pasta entrada crie 3 arquivos vazios:
dados1.txt
dados2.txt
dados3.txt """

from pathlib import Path

caminho_inicial=Path("EXERCÍCIO/Dados/Entrada")
dados=["Dados1.txt",
       "Dados2.txt",
       "Dados3.txt"]


for dado in dados:
    caminho=caminho_inicial / dado
    caminho.touch(exist_ok=True)
