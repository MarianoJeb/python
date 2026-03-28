arquivo=open("CONTEUDO/arquivo.txt")
content=arquivo.read()

print(content)
arquivo.close() ##fechar para evitar problema

##OU
""" with open("CONTEUDO/arquivo.txt") as arquivor:  ##FAZ COM QUE O ARQUIVO FIQUE ABERTO SOMENTE ATÉ O PROGRAMA ACABAR
    print(arquivor.read()) """

""" with open("CONTEUDO/arquivo.txt") as arquivor:
    print(arquivor.readlines()) """

with open("CONTEUDO/arquivo.txt", mode="w", encoding='utf-8') as arquivor:  ##CASO ARQUIVO NÃO EXISTA, ELE É CRIADO
    arquivor.write("Àquele que não conheceu pecado, ele o fez pecado por nós; para que, nele, fôssemos feitos justiça de Deus.")

with open("CONTEUDO/arquivo.txt", mode="a", encoding='utf-8') as arquivor:  ##mode='a' para acrescentar e não substituir
    arquivor.seek(0)
    arquivor.write("2Corintios 5:21")

with open("CONTEUDO/arquivo.txt", mode="r+", encoding='utf-8') as arquivor:  ##mode='r+' para ler e poder editar
    arquivor.write("2Corintios 5:21")
    arquivor.seek(0) ##MUDAR O PONTEIRO PARA O INICIO
    print(arquivor.read())

