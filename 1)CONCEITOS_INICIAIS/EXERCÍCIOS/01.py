#EXERCICIO 01:
#Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.

ano_atual=int(input("Em que ano estamos?: "))
ano_nascimento=int(input("Em que ano você nasceu?:"))
idade=ano_atual-ano_nascimento
print(f"Você tem {idade} anos!!")
if idade>=60:
    print("Tá ficando velho hein!!")
