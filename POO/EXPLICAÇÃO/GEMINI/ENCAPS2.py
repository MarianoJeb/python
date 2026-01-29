###Cenário: Você está criando um sistema de Cofre Eletrônico.

""" O cofre tem um atributo privado __senha (inteiro) e um atributo privado __conteudo (string).
Use @property para o conteudo. Quando alguém tentar ler o conteúdo, o sistema deve pedir (via input ou parâmetro) a senha.
Se a senha estiver correta, retorna o conteúdo.
Se estiver errada, retorna "Acesso Negado".
Crie um método para alterar a senha, mas que exija a senha antiga para validar a troca."""
#Dica: Foque em como o @property pode esconder a lógica de "verificação de segurança" dentro de um simples acesso a atributo. 

class CofreEletronico:
    def __init__ (self,senha:str,conteudo_secreto:str)->None:
        self.__senha=senha
        self.__conteudo=conteudo_secreto
        self.__tentativas:int=3

    @property
    def conteudo(self):

        tentativa=input(f'Digite a sua senha: ')
        if tentativa==self.__senha:
            self.__tentativas=3
            print (f'\nCONTEÚDO:{self.__conteudo}')

        else:
            self.__tentativas-=1

            if self.__tentativas==0:
                print ('VOCÊ USOU TODAS SUAS TENTATIVAS!! ENTRE EM CONTATO COM O SUPORTE.')
                return
            
            print(f'\nSenha errada!\nVocê tem {self.__tentativas} tentativas.')

    @property
    def senha(self):
        return 'Senha privada!'
    
    @senha.setter  
    def senha(self,sla):
        input_senha=input('Digite aqui a sua senha atual:')
        if input_senha!=self.__senha:
            print ('SENHA INCORRETA!!')
        else:
            senha_nova=input('Senha correta!\nDigite aqui sua nova senha:')
            self.__senha=senha_nova
            print('Senha modificada com sucesso!')

sobraNada=CofreEletronico('Sobra nada para o beta','formula magica de como farmar aura e não ser betinha!!!!')

sobraNada.senha='pedro'

