##EXERCÍCIO 03:
""" Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim. """

frase=input("Digite uma frase(cuidado com as palavras!!):\n")
if "bomba" in frase.lower():
    print("CUIDADO, HÁ UMA BOMBA POR PERTO!!")
else:
    print("Pode ficar tranquilo, não há nenhuma bomba!!")   