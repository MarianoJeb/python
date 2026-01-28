##EXERCICIO 01
""" Crie um arquivo matematica.py com as funções:
dobro(numero) → retorna o dobro
metade(numero) → retorna a metade
Crie outro arquivo mensagens.py com a função:
boas_vindas(nome) → imprime uma mensagem de saudação
No arquivo principal (main.py):
Importe as funções dos dois arquivos
Peça ao usuário um número e mostre o dobro e a metade
Dê boas-vindas usando o nome digitado """
########################################################################

from matematica import *
from mensagem import *

nome=input('Qual o seu nome?\n')
numero=int(input(f'{(nome.capitalize())}, digite um número!\n'))
boas_vindas(nome)
print(f'DOBRO:{dobro(numero)}\nMETADE:{(metade(numero)):.2f}')