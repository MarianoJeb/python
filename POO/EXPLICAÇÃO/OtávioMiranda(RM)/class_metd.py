class student:
    COUNT=0
    NOTAS=0

    def __init__(self,nome:str,nota:int)->None:
        self.nome=nome
        self.nota=nota
        student.COUNT+=1
        student.NOTAS+=1

    #INSTANCE METHOD
    def info(self):
        return f'Nome: {self.nome} || Nota: {self.nota}'

    @classmethod
    def counter(cls)->int:
        return f'{cls.COUNT}'
    
    @classmethod
    def media(cls)->float:
        if cls.COUNT==0:
            return 0
        else:
            return f'A média é igual a: {cls.NOTAS/cls.COUNT:.2f}'
    

    