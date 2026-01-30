# Exercício 2 – Quantos meses faltam?
# Crie um programa que exiba quantos meses faltam para o ano acabar.
from datetime import datetime
agora=datetime.now()
meses=(12-agora.month)
print(f"Faltam {meses} meses para o ano acabar!")