#EXERCICIO 02:
#Crie um código onde o usuário deve inserir dois números e exiba a soma, subtração, multiplicação e divisão deles

n1=int(input("Digite um Número:\n"))
n2=int(input("Digite outro Número:\n"))
soma=n1+n2
subtração=n1-n2
multiplicação=n1*n2
divisão=n1/n2
print("As principais operações entre", n1, "e", n2, "são:")
print(f"Soma: {soma}\nSubtração: {subtração}\nMultiplicação: {multiplicação}\nDivisão: {divisão}")
