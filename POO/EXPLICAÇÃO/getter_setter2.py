class Retangulo:
    def __init__ (self,altura:float,largura:float)->None:
        self._altura=altura
        self._largura=largura
    
    @property
    def largura(self)->float:
        return self._largura
    
    @property
    def altura(self)->float:
        return self._altura
    
    @largura.setter
    def largura(self,new_largura)->None:
        if new_largura>0:
            self._largura=new_largura
        else:
            print('Largura deve ser maior que 0!')

    @altura.setter
    def altura(self,new_altura)->None:
        if new_altura>0:
            self._altura=new_altura
        else:
            print('Altura deve ser maior que 0!')
    
    @altura.deleter
    def altura(self):
        del self._altura
        print(f'Altura foi apagada com sucesso')
    
    @largura.deleter
    def largura(self):
        del self._largura
        print('Largura apagada com sucesso')


ret1=Retangulo(13,22)
ret1.altura=0
del ret1.altura