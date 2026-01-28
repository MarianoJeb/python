idade=int(input("Prazer, qual a seua idade?\n"))
if idade<18:
    print("Você é menor de idade!!")
if idade>=18:
    print("Você é maior de idade!!")

senha="rogerio123"
tentativa_senha=input("Qual a sua senha?\n")

if tentativa_senha==senha:
    print("Acesso liberado!!")
if tentativa_senha!=senha:  ## != significa diferente
    print("Acesso negado!!")

if True:
    print("True é verdadeiro, if (se) for verdadeiro, executa o bloco de código!!")

ABC=10<5
if ABC: ##if ABC==True:
    print("10 é menor que 5")
    