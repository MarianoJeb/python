# Exercício 5 – Verificador de evento
# Peça ao usuário que digite uma data de um evento
# Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.
from datetime import datetime


hoje=datetime.now().date()

evento=input('Digite a data no formato dd/mm/aaaa:\n->')
try:
    evento_data=datetime.strptime(evento, "%d/%m/%Y").date()

    if evento_data<hoje :
        print("Poxa, seu evento já passou ):")

    elif evento_data>hoje:
        print(f"Seu evento é daqui a {(evento_data-hoje).day} dia(s)!")

    elif evento_data==hoje:
        print("Corre, corre, corre\nO seu evento já é hoje!")
except ValueError:
    print("Digite uma data válida!")


#OBS: tem que converter para date( .date() ) para que se compare somente a data, n havendo assim a interferencia do horario