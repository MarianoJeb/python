##EXERCICIO 03
""" Estrutura esperada:
perfil/
├── usuario.py
├── validacao.py
main.py

usuario.py → função criar_perfil(nome, idade) → retorna dicionário com os dados
validacao.py → função idade_valida(idade) → retorna True se idade >= 18

main.py :
Recebe os dados do usuário
Valida a idade
Se for válida, cria e exibe o perfil
Senão, exibe uma mensagem de acesso negado """
#################################################################################
from PERFIL import usuario,validacao
nome=input('PRAZER, QUAL O SEU NOME?\n')
idade=int(input('LEGAL,MAS QUAL A SUA IDADE?\n'))
if validacao.validacao(idade)==True:
    user=usuario.criar_perfil(nome,idade)
    print(f'-------CADASTRADO!-------\nNOME:{(user["nome"]).capitalize()} | IDADE: {user['idade']}')
else:
    print("EPA EPA EPA\nVocê é menor de idade!! Acesso negado!!")