##EXERCÍCIO 04:
""" Dada uma variável frase = "    @prendendo @ progr@m@r   "  com espaços nas pontas e letras bagunçadas, o programa deve:
Remover espaços do início/fim
Trocar todas as letras "@" por "a"
Colocar a primeira letra de cada palavra em maiúsculo """

frase="    @prendendo @ progr@m@r   "
print(frase.strip().replace("@", "a").title())