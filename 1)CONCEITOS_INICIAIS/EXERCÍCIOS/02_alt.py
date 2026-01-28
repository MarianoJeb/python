#EXERCICIO 02 (ALTERNATIVO):
#Crie um código onde o usuário deve inserir dois números e exiba a soma, subtração, multiplicação e divisão deles

num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
calculo=[num1+num2, num1-num2, num1*num2, num1/num2]
print(f"AS PRINCIPAIS OPERAÇÕES ENTRE {num1} & {num2} SÃO:")
print(f"SOMA: {calculo[0]}\nSUBTRAÇÃO: {calculo[1]}\nMULTIPLICAÇÃO: {calculo[2]}\nDIVISÃO: {calculo[3]}")