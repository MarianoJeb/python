from func import *
##VARIÁVEIS:
options=0
lista_dados=[]
   
######################################################################################

##PROGRAMA:

while True:
        options=INICIO()
        match options:

                case 1: ##ADICIONAR ALUNO
                        print ("\n-------ADICIONAR ALUNO-------")
                        a=input('NOME DO ALUNO:')
                        b=ler_numero("IDADE DO ALUNO:",int,0,None)
                        c=ler_numero("NOTA DO ALUNO(0 a 10):",float,0,10)
                        dados=adicionar_aluno(a.strip().title(),b,c)
                        lista_dados.append(dados)

                case 2: ##LISTAR ALUNOS:
                        print ("\n-------ALUNOS-------")
                        if len(lista_dados)==0:
                                print("NÃO HÁ ALUNOS NO SISTEMA!")
                        else:
                                listar_alunos(lista_dados)

                case 3: ##BUSCAR ALUNO PELO NOME:
                        print("\n-------PROCURAR ALUNO-------")
                        if len(lista_dados)==0:
                                print('NÃO HÁ ALUNOS NO SISTEMA')
                        else:
                                procurar_aluno(lista_dados)

                case 4: ##REMOVER ALUNO:
                        print ("\n-------REMOVER ALUNO-------")
                        if len(lista_dados)==0:
                                print('NÃO HÁ ALUNOS NO SISTEMA')
                        else:
                                remover_aluno(lista_dados)
                case 5: ##MEDIA ALUNOS:
                        print ("\n-------MÉDIA GERAL-------")
                        if len(lista_dados)==0:
                                print('NÃO HÁ ALUNOS NO SISTEMA')
                        else:
                                media(lista_dados)
                case 6: ##SAIR:
                        break
                case _:
                        print('\nNúmero inválido!\nTente novamente')