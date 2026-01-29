#Getter and Settter

class Teste:
    def __init__(self,valor)->None:
        self._x=valor
    
#Método Getter para retornar valor _x
    @property
    def get_valor(self):
        return self._x
#Método Setter:
    def set_valor(self,valor):
        self._x=valor

pedro=Teste('Pedrinho')
print(f'Valor do objeto: {pedro.get_valor}')

val=input('DIGITE UM VALOR: ')
pedro.set_valor(val)

print(f'Valor do objeto: {pedro.get_valor}')
