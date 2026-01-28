##EXERCICIO 01:
##Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!":
nota_min=7
nota_user=float(input("Qual foi a sua nota no teste?\n"))

if nota_user>=nota_min:
    print("Parabéns! Você Passou!")
else:
    print("infelizmente, você não atingiu a nota mínima.")
