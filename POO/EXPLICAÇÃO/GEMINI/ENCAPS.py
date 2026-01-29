##Sua tarefa:
""" Crie a classe Personagem.
Crie um método chamado receber_dano(quantidade). Esse método deve subtrair a quantidade da __energia.
Certifique-se de que a energia nunca fique abaixo de 0 (se o dano for maior que a energia, ela vira 0).
Crie um método para mostrar a energia atual. """

class Personagem:
    def __init__(self,nome:str,aura:float)->None:
        self.nome=nome.title()
        self.__aura=aura
    
    def receber_dano(self,dano:float)->None:
        nova_aura=(self.__aura-dano)
        self.__aura=max(0,nova_aura)  
        if self.__aura==0:
            print(f'\n{self.nome} recebeu muito dano!!\nEstá com 0 de aura!')
        else:
            print(f'\n{self.nome} perdeu {dano} pontos de aura!!')
    
    def info(self)->None:
        print (f'\nNOME DO PERSONAGEM:{self.nome}\nAURA DO PERSONAGEM:{self.__aura}')


neymar=Personagem('Ney',1000)
neymar.receber_dano(1001)
neymar.info()