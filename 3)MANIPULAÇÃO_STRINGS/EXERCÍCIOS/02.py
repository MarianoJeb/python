##EXERCÍCIO 02:
""" Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices. """

frase=input("FALA RAPAZIADINHA\n Seguinte, fala comigo uma frase:")
count=len(frase)
n1=int(input(f"Seguinte, fala agora um número entre 1 e {count}: "))
n2=int(input("Fala outro: "))
if n1<n2:
    print(frase[n1-1:n2])
else:
    print(frase[n2-1:n1])
