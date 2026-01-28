#LISTAS: variável com varios valores que são mutáveis []
frutas=["maçã", "banana", "kiwi"]
frutas2=frutas.copy()
frutas3=frutas.copy()
frutas4=frutas.copy()
lista=["carro","aviao","moto","bicicleta"]

print(frutas[0])
print(frutas[-1])

##INSERIR ITEM NA LISTA:
frutas.append("manga") #ADICIONA O VALOR AO FINAL DA LISTA
print(frutas)

frutas.insert(1, "abacate") #ADICIONA VALOR AO INDEX DESEJADO (INDEX, VALOR)
print(frutas)

#ALTERAR O VALOR:
frutas[2]="abacaxi"
print(frutas)

#REMOVER ITEM DA LISTA:
fruta_remove=frutas.pop()#REMOVE ITEM CONFORME INDEX || RETORNA ITEM REMOVIDO
print (fruta_remove)

frutas.remove("maçã") #REMOVE ITEM CONFORME NOME
print(frutas)

frutas.clear #LIMPA A LISTA

#FUNÇOES ÚTEIS:
print(len(lista)) #RETORNA A QUANTIDADE DE ITENS NA LISTA

lista2=lista.copy() #COPIA LISTA PARA OUTRA || "=" VAI CRIAR LISTAS ASSOCIADAS
lista3=lista.copy()
lista4=lista.copy()
print(lista)

lista2.sort() #ORGANIZA EM ORDEM (NATURALMENTE ALFEBÉTICA E CRESCENTE)
print(lista2)
lista3.sort(reverse=True) #ORGANIZA EM ORDEM CONTRÁRIA( Z a A || DECRESCENTE)
print(lista3)
lista4.sort(key=len) #ORGANIZA USANDO UMA FUNÇÃO COMO PARÂMETRO (NESSE CASO O TAMANHO)
print(lista4)

print (lista.count("carro")) #RETORNA QUANTIDADE DE VEZES QUE DETERMINADO ITEM APARECE

print(lista.index("carro")) #RETORNA O INDEX DE DETERMINADO ITEM

#UNIR DUAS LISTAS:
frutas2.extend(lista)   #MAIS RÁPIDA
print(frutas2)


for x in lista:         #ÚTIL EM ALGUNS CASOS
    frutas3.append(x)
print(frutas3)


listas_juntas=frutas4+lista    #BOM SABER
print(listas_juntas)

#TUPLAS
#LISTAS, MAS IMUTÁVEIS:
tuplinha=("rogerio", "pedro", "joão")

#TODAS AS FUNÇÕES FUNCIONAM NELA, COM EXEÇÃO AS QUE BUSCAM MUDAR DE ALGUMA MANEIRA O VALOR