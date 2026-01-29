class Microondas:
    def __init__ (self,name:str ,qualidade:str )->None:
        self.name=name
        self.qualidade=qualidade
        self.estado:bool=False

    def ligar(self)->None:
        if self.estado:
            print(f'Microondas ({self.name}) já está ligado!')
        else:
            print(f'Microondas ({self.name}) está ligado agora!')
            self.estado=True

    def desligar(self)->None:
        if self.estado:
            print(f'O Microondas ({self.name}) está desligado agora!')
            self.estado=False
        else:
            print(f'O Microondas ({self.name}) já está desligado!')

    def usar(self,seconds:int)->None:
        if not self.estado:
            print('Você precisa ligar o microondas primeiro!')
        else:
            print(f'Microondas ({self.name}) ligado por {seconds} segundos!')
   
   ##DUNDER METHODS  || MÉTODOS TROVÃO: 
    def __add__ (self, other)->str: ##adição
        return f'{self.name} + {other.name}'

    def __mul__(self, other)->str: ##multiplicação (muda nome do método conforme operação)
        return f'{self.name} * {other.name}'

    def __str__(self)->str:    ##RETORNA UMA STRING E É PRINTADA COM () e str()
        return f'{self.name} (Qualidade:{self.qualidade})'  ##PROUCURA TRAZER INFORMAÇÕES AMIGÁVEIS
    
    def __repr__(self)->str:  ##RETORNA UMA STRING E É MOSTRADA COM O repr() (tbm aparece quando __str__ n é definido) repr vem de REPRESENTATION|| PROCURA TRAZER INFORMAÇÕES MAIS TÉCNICAS
        return f'Microondas(name:"{self.name}", qualidade:"{self.qualidade}")'
    

Samsung:Microondas=Microondas("Samsung",'A')
Brastemp:Microondas=Microondas('Brastemp','C')

print(Samsung+Brastemp)
print(Samsung*Brastemp)

print(Samsung)
print(str(Samsung))
print(repr(Samsung))