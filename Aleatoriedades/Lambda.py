##LAMBDA:
#USADO PARA CRIAR FUNÇÕES EM SOMENTE UMA LINHA

isEven=lambda x:x%2==0
test=int(input('NUMBER:'))
print('IS EVEN' if isEven(test) else 'Not is even')


##USAVEL DENTRO DE FUNCOES PARA SER UM KEY

numbers=[1,2,3,4,5,6,7,8,9,0]
EvenNumbers=filter(isEven, numbers)
print (list(EvenNumbers))

print(sorted(numbers, key=lambda x:x%2==0, reverse=True))
