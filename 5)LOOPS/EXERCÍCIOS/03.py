##EXERCICIO 03
#Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
#Quando o usuário digitar 0, o programa para e mostra o total economizado.
x=int
soma=0
y=0
print('SOMA PORQUINHO (0 PARA CANCELAR)')
while True:
    x = float(input('QUAL O VALOR DO COFRINHO?\n'))
    soma+=x
    if x==0:
        break

""" soma=sum(valores) #FUNC SOMA TODOS OS VALORES DA LISTA
print(f"O dinheiro guardado é igual a {soma}!") """

print(f"O dinheiro guardado é igual a {soma}!")