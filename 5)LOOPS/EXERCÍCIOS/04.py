##EXERCICIO 04
#Crie um sistema de votação onde o usuário escolhe entre:
#1-PIZZA
#2-HAMBURGUER
#3-SAIR
'''Enquanto ele não digitar "3", continue perguntando
No final, mostre quantos votos cada item recebeu'''

print('VOTAÇÃO:\n1-PIZZA\n2-HAMBURGUER\n3-SAIR')
pizza=0
hamburguer=0
while True:
    vot=int(input("DIGITE O SEU VOTO:"))
    match vot:
        case 1:
            pizza+=1
        case 2:
            hamburguer+=1
        case 3:
            break
        case _:
            print("Número inválido")


print(f"PONTUAÇÃO:\nPIZZA:{pizza}\nHAMBURGUER:{hamburguer}")
if pizza>hamburguer:
    print("pizza gannhou!!")
elif hamburguer>pizza:
    print("hamburguer ganhou!!")
else:
    print("EMPATE!!")