#MAGIC METHODS

class Book:
    def __init__(self, title:str, author:str, num_pag:int)->None:
        self.title=title
        self.author=author.title()
        self.num_pag=num_pag
    
    
    def __str__(self)->str:   ##Retorna uma sting representando o objeto para printa (Usado para o usuário ver)
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self)->str:
        return f'Book=title:{self.title}, author:{self.author}, num_pag:{self.num_pag}'
    
    def __eq__(self, other)->bool: ##Compara se dois objetos são iguais
        return self.title==other.title and self.author==other.author
    
    def __lt__(self, other)->bool: ##Les Than (LT) <
        return self.num_pag < other.num_pag
    
    def __gt__(self, other)->bool: ##Greater Than (GT) >
        return self.num_pag > other.num_pag
    ##OPERAÇÕES ARITMÉTICAS:
    def __add__(self, other): ##Addicionar
        return f"{self.num_pag+other.num_pag} pages"
    
    def __sub__(self, other)->str:  ##Subtrair
        return self.num_pag-other.num_pag if isinstance(other, Book) else self.num_pag-other
    
    def __mul__ (self, other): ##Multiplicar
        return self.num_pag*other.num_pag if isinstance(other, Book) else self.num_pag*other
    
    def __truediv__ (self, other): ##Dividir
        return self.num_pag/other.num_pag if isinstance(other, Book) else self.num_pag/other
    ######################################
    def __contains__(self, keyword:str)->bool: ##Contém.
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key=='title':
            return self.title
        elif key=='author': 
            return self.author
        elif key=='num_pages':
            return self.num_pag
        else:
            return f'Key {key} not found...'


book1=Book('Hobbit', 'J.R.R Tolkien', 310)
book2=Book('Harry Potter and the philosopher stone', 'J.K Rowling', 223)
book3=Book('The lion, the witcher, and the wardrobe', 'C.S Lewis', 172)
book4=Book('Hobbit', 'J.R.R Tolkien', 320)

##TENSTING...
print(book1) ##__str__

print(repr(book1)) ##__repr__

print(book1==book4) ##__eq__ (sem isso retornaria False)

print(book1<book2) ##__lt__

print(book1>book2) ##__gt__

#ARITMÉTICOS
print(book1+book2) ##__add__

print(book1-2) ##__sub__

print(book1*8) ##__mul__
#############################
print('Hobbit' in book1) ##__contains__

##__getitem__
print(book1['title']) 
print(book1['author'])
