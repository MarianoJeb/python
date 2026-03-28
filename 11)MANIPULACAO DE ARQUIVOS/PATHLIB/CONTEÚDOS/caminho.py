import shutil
from pathlib import Path
#Path significa literalmente caminho, e é isso q faz, quarda o caminho até o arquivo

##CAMINHOS PODEM SER RELATIVOS OU ABSOLUTOS
#relativos: aponta para arquivo que está na pasta principal
#absoluto: trilha o caminho da primeira pasta do computador até o arquivo(ex:/home/gabriel-mariano/Documents/livro.pdf)

caminho_relativo=Path("arquivinho_lindo.txt")

caminho_absoluto=Path(r"/home/gabriel-mariano/Documents/ACTIVErecall.pdf") #r""->Desconsidera caractéres especiais (\n)

caminho_absoluto_melhorado=Path.home()/"Documents"/"ACTIVErecall.pdf" ##.home()->Faz que seja o home da máquina, funcionando tanto em um linux, windows, ou mac, mesmo tendo arquiteturas diferentes

caminho_relativo_convertido=caminho_relativo.absolute() #Converte um caminho relativo para um absoluto


caminho_inexistente=Path("arquivo_inexistente.txt")
if not caminho_inexistente.exists():  ##exists()==existe
    print("Ñ existe ")

if caminho_relativo.is_file():
    print("É um arquivo")

elif caminho_relativo.is_dir():  ##dir==diretorio
    print("É Um Diretório/Pasta")


######CRIAR PASTAS DINÂMICAMENTE######
""" new_folder=Path("New Folder")
new_folder.mkdir(exist_ok=True) """ ##Se a pasta/arquivo já existir, não lança um erro

#criar pasta dentro de pasta:
""" pastas=Path("NOVAPASTA/PASTA/P")
pastas.mkdir(exist_ok=True, parents=True) ##Parents=True """


######DELETAR AQUIVOS######
novapasta=Path("NOVAPASTA")
arquivinho=Path("CONTEÚDOS/arquivinho_lindo.txt")

""" novapasta.unlink()""" #DESLINKAR (deleta) somente arquivos 

""" novapasta.Path.rmdir() """ #Remove diretórios apenas se estiver vazio

""" shutil.rmtree(novapasta) """  #Remove Tree(arvore)/diretorios com arquivos dentro

######LENDO/ESCREVENDO ARQUIVO######
#ESSA BIBLIOTECA RARAMENTE É USADA PARA ISSO

#LENDO
""" texto=arquivinho.read_text(encoding="utf-8") """  ##enconding="utf-8" evita erros de caractéres
""" print(texto) """

#ESCREVENDO
""" arquivinho.write_text("Pedro e Ana\nJoão e Maria", encoding="utf-8") """

######MOSTRA ARQUIVOS NA PASTA######
a=Path("")
conteudos=Path("PATHLIB/CONTEÚDOS")
for arquivo in conteudos.iterdir(): ##ITERAR O DIRETÓRIO
    print (arquivo)

print('\n')

for ana in conteudos.glob("*.txt"): ##FILTRA OQ VAI RETORNAR
    print(ana)

print('\n')

for pedro in a.rglob("*.txt"): ##FILTRA OQ VAI RETORNAR/ vê subpastas
    print (pedro)

print(f"NOME:{arquivinho.name} \nNOME LIMPO: {arquivinho.stem} \nTIPO: {arquivinho.suffix}")




######CRIAR ARQUIVO LIMPO######

arquivo_novo=Path("arquivo_novo.txt")
arquivo_novo.touch()