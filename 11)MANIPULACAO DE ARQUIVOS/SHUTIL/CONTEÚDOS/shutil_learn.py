import shutil 
from pathlib import Path

##TREE == DIRETÓRIO

""" shutil.copy("ARQUIVOS/exemplo.txt", "EXEMPLO_folder/exemplo.txt") ##ARQUIVO

#shutil.copy2  ##MSM COISA, COPIA OS METADADOS

shutil.copytree("ARQUIVOS", "ARQUIVOSbackup", dirs_exist_ok=True)  ##SE JÁ EXISTE, N DÁ ERRO

arquivo=Path("arquivoTESTE.txt")
#shutil.move(arquivo, "ARQUIVOS",) 

#shutil.move("ARQUIVOS/pedro.xlsx", "ARQUIVOS/maria.xlsx")  TBM PODE SER USADO PARA MUDAR O NOME

shutil.rmtree("ARQUIVOSbackup")  ##remove a pasta

shutil.make_archive("ARQUIVOS", "zip", "ARQUIVOS")  ##ARQUIVO/FORMATO/NOME DO NOVO ARQUIVO REMODELADO

shutil.unpack_archive("ARQUIVOS.zip", "ARQUIVOSnovos") """

#EXEMPLO

arquivos=Path("ARQUIVOS")
arquivos_backup=Path("BACKUP_ARQUIVOS")

if not arquivos_backup.exists():
    arquivos_backup.mkdir(parents=True)

shutil.copytree("ARQUIVOS", "BACKUP_ARQUIVOS", dirs_exist_ok=True)
