class Canal:  ##CLASSEEEE
    ##funções dentro de uma classe é um método
    ##__init__ método padrão do python (método mágico/construtor)
    def __init__(self,nome,descricao,inscritos):
        ##tODO MÉTODO DENTRO DE UMA CLASE RECEBE O SELF COMO PARÂMETRO
        self.nome=nome
        self.descricao=descricao
        self.incritos=inscritos
        self.videos=[]
        self._playlists=[]

    def postar(self,video):
        if video in self.videos:
            print('Vídeo já foi postado!!')
            return
        self.videos.append(video)
    ##CRIANDO UM MÉTODO
    def inscrever(self,quant=1):
        self.incritos+=quant

    def remove_playlist(self,playlist):
        if playlist not in self._playlists:
            print('Playlist não existente!!')
        else:
            self._playlists.remove(playlist)

    def mostrar_playlist(self): ##MOSTRA AS PLAYLISTS E OS VIDEOS DELAS
        if len(self._playlists)==0:
            print (f'O canal {self.nome} não tem playlists')
            return
        
        for playlist in self._playlists:
            print('==============================')
            print (f'NOME PLAYLIST: {playlist}')
            print('==============================')
            playlist.most_video()
    
    def add_playlist(self, playlist):
        if playlist in self._playlists: 
            print(f'Playlist {playlist} já está no canal!')
            return
        self._playlists.append(playlist)
        


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
    def __init__ (self,titulo,descricao,data_pub):
        self.titulo=titulo
        self.descricao=descricao
        self.data_pub=data_pub

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
DATA PUBLICAÇÃO: {self.data_pub}
VISUALIZAÇÕES: {self.views}
LIKES: {self.likes} | DESLIKES: {self.deslikes}
COMENTARIOS: {self.coment}""")



class Playlist:
    def __init__(self,titulo):
        self.titulo=titulo

        self._videos=[]

    def __repr__ (self):
        return f'<{self.titulo}>'

    @property
    def videos_playlist(self):
        return self._videos
    
    def add_videos(self,video):  ##ADICIONAR VÍDEO
        if video in self._videos:
            print('Vídeo já está na playlist!')
            return
        self._videos.append(video)

    def remov_video(self,video):  ##REMOVE VIDEO
        if video not in self._videos:
            print('Vídeo não está na playlist!!')
        else:
            self._videos.append(video)

    def most_video(self):  ##MOSTRAR VÍDEOS
        if len(self._videos)==0:
            print('Não há vídeos na playlist!')
            return
        for video in self._videos:
            print(f"""TÍTULO: {video.titulo} 
DESCRIÇÃO: {video.descricao}
DATA PUBLICAÇÃO: {video.data_pub}
VISUALIZAÇÕES: {video.views}
LIKES: {video.likes} | DESLIKES: {video.deslikes}
COMENTARIOS: {video.coment}
============================""")

canal_lancode=Canal('Lan Code','Códigos e gatos', 41000)
canal_guanabara=Canal('Curso em vídeo', 'Paixão por ensinar', 2500000)
canal_manual_mundo=CanalEmpresarial('Manual do Mundo', 'UM MANUAL PRO MUNDO', 20000000)

video_veleiro=Videos('Veleiro Episódio Final','Fiz um veleiro e olha no que deu','01/01/2025' )
video_basico=Videos('Como construir uma bomba atômica em casa','Trump n pode saber disso', '6/12/2003')
video_biscoito=Videos('Como fazer um biscoito com 3 ingredientes','bicoitinho fácil', '03/03/2020')

canal_manual_mundo.postar(video_basico)
canal_manual_mundo.postar(video_veleiro)

videos_loucos=Playlist('Vídeos loucosss')
videos_loucos.add_videos(video_basico)
videos_loucos.add_videos(video_veleiro)

videos_receitas=Playlist('Videos Receitas')
videos_receitas.add_videos(video_biscoito)

canal_manual_mundo.add_playlist(videos_receitas)
canal_manual_mundo.add_playlist(videos_loucos)
canal_manual_mundo.mostrar_playlist()