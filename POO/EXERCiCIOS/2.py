##EXERCÍCIO 02:
#2-Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)

import time

#Exeções
class nome_curto(Exception): pass
class idade_min(Exception): pass



class book:
    def __init__(self,titulo:str,autor:str):
        self.titulo=titulo.title()
        self.autor=autor.title()
    def __str__(self):
        return f'Título:{self.titulo}\n-Autor:{self.autor}'

class library:

    def __init__(self,nome:str):
        self.nome=nome
        self.livros=[]
        self.livros_emprestados=[]

    def add_livro(self,*livros:tuple):
        for livro in livros:
            livror=book(*livro)
            self.livros.append(livror)
        

    #VER LIVROS DA BIBLIOTECA
    def view_book(self)->None:
        if len(self.livros)==0:
            print('Não há livros na biblioteca!!\n):')
            return

        print('\n---Lista de Livros---')
        for i,book in enumerate(self.livros, 1):
            print(f'{i}-{book}')

class cliente:
    def __init__(self,nome:str, idade:int)->None:
        self.nome=nome.title().strip()
        self.idade=idade
        self.livros_pegos=[]
    
    #PEGAR LIVRO DA BIBLIOTECA
    def take_book(self, livro:int, biblioteca:library)->None:
        if len(biblioteca.livros)==0:
            print('Não há livros na biblioteca!')
            return
        biblioteca.livros_emprestados.append(biblioteca.livros[livro-1])
        self.livros_pegos.append(biblioteca.livros[livro-1])
        print(f'\nLivro pego: {biblioteca.livros[livro-1].titulo}')
        print(f'Voltando a tela inicial...')
        time.sleep(3)
        biblioteca.livros.pop(livro-1)
        

    #DEVOLVER LIVRO A BIBLIOTECA:
    def return_book(self, biblioteca:library)->None:
        if len(self.livros_pegos)==0:
            print('\nVocê ainda não pegou nenhum livro na biblioteca!!')
            print('Voltando a tela inicial...')
            time.sleep(3.0)
            return
        print(f'\n{"="*4}DEVOLVER LIVRO{"="*4}')
        for i,livro in enumerate(self.livros_pegos,1):
            print(f'{i}-{livro.titulo}')
        print(f'{"="*20}')
        print(f'{i+1}-Voltar')

        try: choice=int(input('->'))
        except (ValueError, IndexError):

            print('ERRO:\nValor inválido!')
        if choice==(i+1):
            return
        if choice>len(self.livros_pegos):
            print('❌ERRO:\nLivro não encontrado!')
            time.sleep(3)
            return
        biblioteca.livros.append(self.livros_pegos[choice-1])
        biblioteca.livros_emprestados.pop(choice-1)
        print(f'O livro {self.livros_pegos[choice-1].titulo}, foi devolvido a biblioteca!!')
        self.livros_pegos.pop(choice-1)
        time.sleep(3)
    

    def info(self):
        print('\n------INFORMAÇÕES------')
        print(f'Nome: {self.nome} | Idade: {self.idade}')
        time.sleep(2.0)
        
    



def cadastro()->cliente:
    while True:
        try:
            print('\n---CADASTRO---')
            name=input('DIGITE AQUI O SEU NOME:')
            if len(name)<3:
                raise nome_curto
            
            idade=int(input('DIGITE AQUI A SUA IDADE:'))
            if idade<18:
                raise idade_min
            
            user=cliente(name,idade)
            return user
        
        except ValueError :
            print('❌ERRO:\nValor inválido!')
        except nome_curto:
            print('❌ERRO:\nNome muito curto!')
        except idade_min:
            print('❌ERRO\nNão é possível criar uma conta sendo menor de idade!')

biblioteca_do_jorge=library('Biblioteca do Seu Jorge')

biblioteca_do_jorge.add_livro(["Dom Casmurro", "Machado de Assis"], ["1984", "George Orwell"],
    ["O Hobbit", "J.R.R. Tolkien"], ["A Hora da Estrela", "Clarice Lispector"],
    ["O Alquimista", "Paulo Coelho"], ["Ensaio sobre a Cegueira", "José Saramago"],
    ["Harry Potter", "J.K. Rowling"], ["O Pequeno Príncipe", "Antoine de Saint-Exupéry"],
    ["Drácula", "Bram Stoker"], ["Sherlock Holmes", "Arthur Conan Doyle"])
    


def main(biblioteca:library, user:cliente)->None:
        
        

        biblioteca.add_livro(["Dom Casmurro", "Machado de Assis"], ["1984", "George Orwell"],
        ["O Hobbit", "J.R.R. Tolkien"], ["A Hora da Estrela", "Clarice Lispector"],
        ["O Alquimista", "Paulo Coelho"], ["Ensaio sobre a Cegueira", "José Saramago"],
        ["Harry Potter", "J.K. Rowling"], ["O Pequeno Príncipe", "Antoine de Saint-Exupéry"],
        ["Drácula", "Bram Stoker"], ["Sherlock Holmes", "Arthur Conan Doyle"])

        while True:
            total_livros=len(biblioteca_do_jorge.livros)

            opcoes=['Devolver Livro', 'Ver Perfil', 'Sair']
            print(f'\n------{biblioteca_do_jorge.nome.upper()}------')

            for i, livro in enumerate (biblioteca_do_jorge.livros, 1):
                print(f'{i}-{livro}')

            print(f'{"="*30}')
            print(f'{total_livros+1}-{opcoes[0]}\n{total_livros+2}-{opcoes[1]}\n{total_livros+3}-{opcoes[2]}')

            try: choice=int(input('->'))
            except Exception:
                print('ERRO:\nDigite um valor válido!')

            if 1<=choice<=total_livros:
                user.take_book(choice,biblioteca_do_jorge)
            elif choice==total_livros+1:
                user.return_book(biblioteca_do_jorge)
            elif choice==total_livros+2:
                user.info()
            elif choice==total_livros+3:
                print('Obrigado pela visita!!')
                break
            else:
                print('Digite uma ação válida!!')
                time.sleep(3)


biblioteca_do_jorge=library('Biblioteca do Seu Jorge')
usuario=cadastro()
main(biblioteca_do_jorge, usuario)
