##EXERCICIO 03
""" Crie uma função chamada verificar_par(numero) que retorna:
"Par" se o número for par
"Ímpar" se for ímpar
Peça um número ao usuário com input(), chame a função e mostre o resultado. """

##FUNÇÃO:
def verifica_par(num):
    if num%2==0:
        return ('PAR')
    else:
        return("IMPAR")

##MUITO ÚTIL:
while True:
    try: #TENTE ISSO:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError: #SE DER ERRO NO VALOR, FAZ ISSO
        print("Entrada inválida! Por favor, digite um número inteiro válido.")
        print('')

print(verifica_par(numero))