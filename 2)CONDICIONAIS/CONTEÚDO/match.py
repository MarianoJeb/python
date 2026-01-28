numero=int(input("Digite o número de 1 a 3:\n"))
match numero:
    case 1:
        print("VOCê DIGITOU 1")
    case 2:
        print("VOCÊ DIGITOU 2")
    case 3:
        print("VOCÊ DIGITOU 3")
    case _:
        print("NUMERO INVÁLIDO!!")

#CASE_ O CORINGA, CASO NENHUMA DAS OPÇÕES SEJAM ATENDIDAS

nota=int(input("digite dua nota de 0 a 10:\n"))
match nota:
    case 9 | 10:
        print("SHOW")
    case 7 | 8:
        print("MUITO TOP")
    case 5 | 6:
        print("PODE MELHORAR")
    case 4 | 3 | 2 | 1 | 0:
        print("ESTUDE MAIS NA PRÓXIMA VEZ!!")
    case _:
        print("NOTA INVÁLIDA!!")

#USO DO | PARA REPRESENTAR O "OU" DENTRO DO MATCH CASE ("OR" NÃO FUNCIONA AQUI)