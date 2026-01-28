contador=1
while contador<=5:
    print(contador)
    contador+=1

senha=''
while senha != 'neymar':
    senha=input("DIGITE SUA SENHA:")
print ('Senha correta!!')

for numero in range(1,5):
    print(numero)

frutas=["maçã", 'melancia', 'banana']
for fruta in frutas:
    print (f"fruta: {fruta}")

for mult in range(1,11):
    for mults in range (1,11):
        print(f'{mult}*{mults} = {mult*mults}')
        if mults ==10: #SÓ PARA SEPARAR
            print('')

pessoas=["messi",'neymar','rogerio ceni', 'ribamar', 'pelé', 'chaves']
for nome in pessoas:
    print(f'procurando... \n{nome}')
    if nome=='ribamar':
        print('nome encontrado: RIBAMAR')
        break  #BREAK ACABA O LOOP QUANDO CONDIÇÃO FOR ALCANÇADA

print('busca encerrada')

for numero in range(1,11):
    if numero%2 == 0:
        continue #CONTINUE 'PULA A VEZ' SE A CONDIÇÃO FOR VERDADEIRA 
    print(numero)

for letra in "melancia":
    if letra == "n":
        break
    print (letra)