#EXERCICIO 06:
"""Crie um menu com 3 opções:
-Pizza
-Sushi
-Salada
O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: Opção inválida."""


print("MENU:\n1-Pizza\n2-Sushi\n3-Salada")
opcao=int(input("Digite o número da sua escolha:\n"))
match opcao:
    case 1:
        print("PIZZA!!")
    case 2:
        print("SUSHI!!")
    case 3:
        print("SALADA!!")
    case _:
        print("OPÇÃO INVÁLIDA!!")