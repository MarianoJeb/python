#EXERCICIO 05|DICIONÁRIOS
""" Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
Depois, verifique se a idade é maior ou igual a 18:
Se sim, imprima: "Acesso liberado para {nome}"
Se não, imprima: "Acesso negado para {nome}" """

dados={
    "nome": input("Prazer, qual o seu nome?\n"),
    "idade": int(input(f"Que bom te conhecer! mas qual a sua idade?\n"))
    
}
if dados["idade"]>18:
    print(f"ACESSO LIBERADO PARA {dados['nome'].upper()}!")
else:
    print(f"ACESSO NEGADO PARA {dados['nome'].upper()}")