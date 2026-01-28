frase="olá mundo!"
print(frase[2]) #vai printar o index 2(á)
print(frase[-0]) #numeros negativos funcionam de trás para frente
print(frase[2:6]) #vai printar do index 2 (á) até o index 5 (o último número é ignorado/-1)
print(frase[:6]) #vai printar do início até o index 5

print(len(frase)) #Quantidade total de caracteres da string
print(frase.count("o")) #Quantidade de caracter especifico
print(frase.find("o")) #Index do caracter especifico
print("\n")

if "mundo" in frase:
    print('"mundo" está na frase')
else:
    print('Não tem "mundo" na frase')

print (frase.lower())
print (frase.upper())

print("\n")

print(frase.capitalize())  #A primeira letra fica maiúscula

frase2='     RAPAZ     '
print(frase2.strip())
#Tira os espaços laterais

print(frase2.replace("A", "O")) #Muda a primeira letra entre as chaves pela segunda

print(frase.title()) #Primeira letra de cada palavra em maiúsculo