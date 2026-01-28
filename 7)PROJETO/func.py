def INICIO():
        while True:
                try:
                        print ('\n'+"="*30)
                        print('        SISTEMA ESCOLA:')
                        print (''+"="*30)
                        numero=int(input('\n1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair\n-'))
                        return numero
                except ValueError:
                        print('\nValor inválido! \nDigite um número!')

#ADICIONAR ALUNO
def adicionar_aluno(nome,idade,nota):
    
        dados={
        'nome':nome,
        'idade':idade,
        'nota':nota
    }
        return dados
#LER SE É UMA ENTRADA POSSÍVEL(Número)
def ler_numero(mensagem,tipo,val_min,val_max):
        while True:
                try:
                        valor=tipo(input(mensagem))
                        
                        if (val_min or val_max)!=None and (valor<val_min or val_max<valor):
                                print("Número inválido!")
                                continue #Volta para o início do loop

                        return valor #Se tudo deu certo, vai retornar o valor
                
                except ValueError:
                        print('ENTRADA INVÁLIDA\nDigite novamente!')
                        print('')

#LISTAR ALUNOS:
def listar_alunos(lista):
        for aluno in lista:
                print(f"Aluno:{aluno['nome']} | Idade:{aluno['idade']} | Nota:{aluno['nota']}")

#PROCURAR ALUNO:
def procurar_aluno(a):
        aluno_input=input('NOME DO ALUNO:')
        print('\nProcurando...')
        for aluno in a:
                if aluno["nome"].lower()==aluno_input.strip().lower():
                        print(f"Aluno encontrado:{aluno['nome']}")
                        print(f"Aluno:{aluno['nome']} | Idade:{aluno['idade']} | Nota:{aluno['nota']}")
                        break
        else:
                print('ALUNO NÃO EXISTENTE!')

#REMOVER ALUNO
def remover_aluno(lista):
        nome_aluno=input('NOME ALUNO:')
        print('PROCURANDO...')
        for aluno in lista:
                if aluno['nome']==nome_aluno.strip().title():
                        lista.remove(aluno)
                        print(f"O ALUNO {aluno['nome']} FOI REMOVIDO!")
                        break
        else:
                print('ALUNO NÃO EXISTENTE!')

#CALCULAR MEDIA
def media(lista):
        nota=0
        for notas in lista:
                nota+=notas['nota']
        media=nota/len(lista)
        print(f'MÉDIA GERAL DOS ALUNOS:{media:.2f}') #:.2f SERVE PARA LIMITAR A DUAS CASAS DECIMAIS