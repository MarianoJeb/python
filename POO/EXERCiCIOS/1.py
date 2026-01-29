""" 1-Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada) """
class nome_curto(Exception):
    pass

class idade_min(Exception):
    pass

class Destino:
    def __init__(self,Lugar:str):
        self.lugar=Lugar
    
    def __str__(self):
        return f'{self.lugar}'

class Destinos:
    def __init__(self):
        self.destinos=[]

class Order():
    def __init__(self):
        self.order=[]

    def add_iten(self,new):
        self.order.append(new)
    
    def view_order(self):
        if len(self.order)==0:
            print('Não há destinos definidos!!')
            return
        print('\n---VÔOS DEFINIDOS---')
        for i,thing in enumerate(self.order, 1):
            print(f'{i}-{thing}')

class Viajante:
    def __init__(self,name:str, idade:int):
        self.name=name.title()
        self.idade=idade
        self.order
        

    def order(self, order):
        self.order=order
    
    def info (self):
        print("---INFORMAÇÕES---")
        print(f'Nome:{self.name} | Idade:{self.idade}')

def cadastro():
    while True:
        try:
            print('\n---CADASTRO---')
            name=input('DIGITE AQUI O SEU NOME:')
            if len(name)<3:
                raise nome_curto
            
            idade=int(input('DIGITE AQUI A SUA IDADE:'))
            if idade<18:
                raise idade_min
            
            viajante=Viajante(name,idade)
            return viajante
        
        except ValueError :
            print('Valor inválido!')
        except nome_curto:
            print('Nome muito curto!')
        except idade_min:
            print('Não é possível criar uma conta sendo menor de idade!')


ordem=Order()
lista=Destinos()
lista.destinos=[Destino('GRAMADO-RS'),
                    Destino('PORTO SEGURO-BA'),
                    Destino('SALVADOR-BA'),
                    Destino('VITÓRIA-ES'),
                    Destino('BRASÍLIA-DF')]

def main():
    while True:
        print('\n---DESTINOS DISPONÍVEIS---')
        for i,destino in enumerate(lista.destinos, 1):
            print(f'{i}-{destino.lugar}')
        print(f'{i+1}-VER MEUS DESTINOS')
        print(f'{i+2}-VER PERFIL\n{i+3}-SAIR')

        try :choice=int(input('->'))
        except ValueError:

            print('Digite um número válido!')
        if choice in range(1,i+1):
            ordem.add_iten(lista.destinos[choice-1])
        elif choice==(i+1):
            ordem.view_order()
        elif choice==(i+2):
            viajante.info()
        elif choice==(i+3):
            break
        else:
            print('Digite um número disponível!!')

viajante=cadastro()
main()