""" Crie um script que:
Verifica se existe um arquivo chamado relatorio.txt.
Move esse arquivo para uma pasta chamada relatorios_antigos.
Durante a movimentação, renomeie o arquivo para relatorio_backup.txt. """

import shutil
from pathlib import Path


##CRIANDO PASTA DE RELATÓRIOS ANTIGOS
relatorios_antigos=Path("EXERCICIOSzz/RELATORIOS ANTIGOS")
relatorios_antigos.mkdir(exist_ok=True, parents=True)

##VERIFICANDO EXISTENCIA do ARQUIVO
relatorio=Path("relatorio.txt")
if relatorio.exists():
    ##MOVENDO ARQUIVO
    shutil.move(relatorio, relatorios_antigos/"relatorio_backup.txt")
else: print('ARQUIVO Ñ ENCONTRADO ):')