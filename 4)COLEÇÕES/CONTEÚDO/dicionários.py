pessoa={
    "nome":"Pedro",
    "idade":25,
    "cidade":"Belém",
    "profissão":["pintor", "bispo", "espadeiro"] #É POSSÍVEL COLOCAR LISTAS DENTRO DE UM DICIONÁRIO
}
print(pessoa["profissão"][0])
print(pessoa["cidade"])

pessoa["idade"]=26 #MUDA O VALOR

del pessoa["cidade"] #REMOVE O VALOR

print(pessoa.keys())  #RETORNA AS CHAVES
print(pessoa.values()) #RETORNA OS VALORES

valores=list(pessoa.values()) #COLOCA OS VALORES(values)/KEYS(keys) EM UMA LISTA
print(valores)

print(pessoa.items()) #RETORNA OS ITENS / Ñ PODE SER COLOCADO EM LISTA (tipo em cima)

print(pessoa.get("telefone", "Não existe")) #TESTA SE TEM A CATEGORIA, SE NÃO TIVER, RETORNA "None" OU A MENSAGEM APÓS ,

valor_removido=pessoa.pop("profissão") #REMOVE E RETORNA OQ REMOVEU
print(valor_removido)
print(pessoa)

#exemplo:
produto={
    "nome":"Celular",
    "valor":2500,
    "estoque":12

}

print(f"O produto {produto["nome"]} com o valor {produto["valor"]}, tem {produto['estoque']} itens no estoque!")