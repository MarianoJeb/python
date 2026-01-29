class Canal:  ##CLASSEEEE
    ##funções dentro de uma classe é um método
    ##__init__ método padrão do python (método mágico/construtor)
    def __init__(self,nome,descricao,inscritos):
        ##tODO MÉTODO DENTRO DE UMA CLASE RECEBE O SELF COMO PARÂMETRO
        self.nome=nome
        self.descricao=descricao
        self.incritos=inscritos
        self.videos=[]

    def postar(self,video):
        if video in self.videos:
            print('Vídeo já foi postado!!')
            return
        self.videos.append(video)
    ##CRIANDO UM MÉTODO
    def inscrever(self,quant=1):
        self.incritos+=quant




class CanalEmpresarial(Canal):  #HERANÇA
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos) ##herda coisas da outra classe
        self._equipe=[] ##ENCAPSULAMENTO(usar o _ antes)
    
    @property #O PYTHON ENTENDE COMO UMA PROPIEDADE E TIRA A NECESSIDADE DE ()
    def equipe(self):
        return self._equipe
    
    def adicionar_membro(self,membro): ##MÉTODO PARA ADICIONAR MEMBRO NA EQUIPE
        if membro not in self._equipe:
            self._equipe.append(membro)
        else: print(f'O membro {membro} já está na equipe!!')

    def remove_membro (self,membro): ##MÉTODO PARA REMOVER
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print('Membro não está na equipe!!')



class Videos:
    def __init__ (self,titulo,descricao):
        self.titulo=titulo
        self.descricao=descricao

        self.views=0
        self.likes=0
        self.deslikes=0
        self.coment=[]
##MÉTODOS (:
    def __repr__(self):
        return f'<{self.titulo}>'
    
    def assistir(self):
        self.views+=1

    def gostar(self):
        self.likes+=1

    def n_gostar(self):
        self.deslikes+=1

    def comentar(self,comentario):
        self.coment.append(comentario)

    def info(self):
        print(f"""TÍTULO: {self.titulo} 
DESCRIÇÃO: {self.descricao}
VISUALIZAÇÕES: {self.views}
LIKES: {self.likes} | DESLIKES: {self.deslikes}
COMENTARIOS: {self.coment}\n""")


canal_lancode=Canal('Lan Code','Códigos e gatos', 41000)
canal_guanabara=Canal('Curso em vídeo', 'Paixão por ensinar', 2500000)
canal_manual_mundo=CanalEmpresarial('Manual do Mundo', 'UM MANUAL PRO MUNDO', 20000000)

video_veleiro=Videos('Veleiro Episódio Final','Fiz um veleiro e olha no que deu' )
video_basico=Videos('Como construir uma bomba atômica em casa','Trump n pode saber disso')

canal_manual_mundo.postar(video_basico)
canal_manual_mundo.postar(video_veleiro)
print(canal_manual_mundo.videos)