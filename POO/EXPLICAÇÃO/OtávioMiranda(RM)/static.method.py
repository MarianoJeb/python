class Calculator:
    def __init__ (self, model:int)->None:
        self.model=model

    def info(self):
        return f'Calculadora Modelo: {self.model}'

    @staticmethod #Ñ PRECISA MAS FICA BONITO
    def somar(*numeros:float)->float:
        return f'SOMA: {sum(numeros)}' #sum Soma números de uma Lista ou Tupla
        ##é um método que não precisa estar dentro da classe/ não depende dela


if __name__ == '__main__':  ##SERVE PARA QUE VARIAVEL/FUNCS(etc...) NÃO POSSAM SER EXPORTADO
    calc1=Calculator(96)
    print(calc1.info())
    print(calc1.somar(1,2,4,5,6,7,8,9))


################################################################################################

from datetime import date

class Person:
    def __init__ (self,name:str,idade:int):
        self.name=name
        self.idade=idade

    def info(self)->str:
        return f'NOME: {self.name} ||IDADE: {self.idade}'
    
    @classmethod
    def ano_nasc(cls,nome:str,ano:int):
        ano_atual=date.today().year  ##função da bibliteca
        idade=ano_atual-ano
        return cls(nome, idade)
    

person1=Person.ano_nasc('Pedrin', 1945)
print(person1.info()) 