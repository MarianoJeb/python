""" Liste todos os arquivos .txt dentro de entrada.
Imprima apenas o nome do arquivo (sem o caminho completo) """

from pathlib import Path

entrada=Path("EXERCÍCIO/Dados/Entrada");
print("------ENTRADA------")
for i, arquivo in enumerate(entrada.glob("*.txt"), start=1):
    print(f"{i}-{arquivo.name}")