##EXERCICIO 02
#Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

numeros=[]

for numero in range(5):
    if numero==0:
        numeros.append(int(input("Digite um número: ")))
    else:
        numeros.append(int(input("Digite outro número: ")))
    
#soma=sum(numeros) #SOMA OS VALORES DA LISTA
soma=0
for numero in numeros:
    soma+=numero
print(f"A soma total é igual a {soma}")

########################################################################################

result=0
for num in range(5):
    num=int(input("Fale um número: "))
    result+=num
print(f"Resultado simplificado:{result}")
