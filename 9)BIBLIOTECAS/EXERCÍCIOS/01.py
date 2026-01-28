##EXERCÍCIO 01:
""" Crie um programa que sorteia um número inteiro entre 1 e 10 usando a biblioteca random.
O jogador tem que tentar adivinhar esse número.
O jogo deve continuar perguntando até o jogador acertar.
-A cada tentativa, o programa deve informar:
"Muito alto!" se o palpite for maior que o número sorteado
"Muito baixo!" se for menor
"Acertou!" se for igual
Ao final, informe quantas tentativas foram necessárias para acertar """

########################################################################

import random
x=0
numero_aleatorio=random.randint(1,10)
while True:
    print("\n-------ADVINHE O NÚMERO-------")
    numero_input=int(input('DIGITE O NÚMERO:'))
    if numero_input == numero_aleatorio and x==0:
        print('NOSSA, VOCÊ ACERTOU DE PRIMEIRA!!')
        break
    
    if numero_aleatorio>numero_input:
        print('QUASE! DIGITE UM NÚMERO MAIOR!!')
        x+=1
        continue
    
    if numero_aleatorio<numero_input:
        print('QUASE! DIGITE UM NÚMERO MENOR!!')
        x+=1
        continue
    
    if numero_input == numero_aleatorio:
        print('\nPARABÉNS, VOCÊ ACERTOU!!')
        print(f'TENTATIVAS:{x+1}')
        break
    