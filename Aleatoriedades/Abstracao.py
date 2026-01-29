#ABSTRAÇÃO
from abc import ABC, abstractmethod

class automovel(ABC):  ##SERVE APENAS COMO MODELO, E PARA SER HERDADO EM OUTRAS CLASSES, TODOS OS METODOS DEVEM SER INSTANCIADOS!!
    def __init__(self,model:str,quant_rodas:int):
        self.model=model.title()
        self.rodas=quant_rodas
        self.ligado=False
    @abstractmethod
    def ligar(self):
        if self.ligado==True:
            print(f'{self.model} já está ligado!!')
        else:
            self.ligado=True
            print(f'{self.model} ligado!')


class Carro(automovel):
    def __init__(self, model, quant_rodas):
        super().__init__(model, quant_rodas)
    def ligar(self):
        return super().ligar()
    
pedro=Carro('Ferrari',4)
pedro.ligar()