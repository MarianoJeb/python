""" Crie a seguinte estrutura:
├──dados/
│  ├── entrada/
│  └── saida/
├──relatorios/
Crie todas as pastas em uma única execução do seu código. """

from pathlib import Path

pasta_mae="EXERCÍCIO"
folders=[Path("EXERCÍCIO/Dados/Entrada"), Path("EXERCÍCIO/Dados/Saida"), Path("EXERCÍCIO/Relatorios")]

for folder in folders:
    folder.mkdir(exist_ok=True, parents=True) ##Parents tbm cria as pastas pai caso n exista


