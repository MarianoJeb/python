##EXERCICIO 04:
""" Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:
Nota 9 ou 10: Excelente!
Nota 7 ou 8: Muito bom
Nota 5 ou 6: Regular
Menor que 5: Ruim """

print("AVALIE MEGAMENTE 2:")
nota=int(input("Digite a sua nota de 0 a 10:\n"))
if nota==9 or nota==10:
    print("EXCELENTE!!")
elif nota==7 or nota==8:
    print("MUITO BOM!!")
elif nota==5 or nota==6:
    print("REGULAR!!")
else:
    print("RUIM!!")