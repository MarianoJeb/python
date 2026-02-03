# Exercício 4 – Contagem regressiva para o fim do ano
# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

from datetime import datetime, timedelta

hoje=datetime.now().date()
fimAno=datetime(day=31, month=12, year=hoje.year).date()
faltam=(fimAno-hoje)

print(f"Faltam {faltam.days} dias para acabar o ano!")