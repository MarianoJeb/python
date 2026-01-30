# Exercício 3 – Assinatura digital do terminal
# Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:
# Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 12:30
from datetime import datetime
import locale ##Serve para deixar em portugûes (:

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

name=input("----ASSINATURA DIGITAL----\nNome:").title()
hora=datetime.now()

print(hora.strftime(f"Assinatura gerada por {name} em %d de %B de %Y às %H:%M"))