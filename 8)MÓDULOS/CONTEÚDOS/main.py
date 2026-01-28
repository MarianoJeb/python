import funcoes ##IMPORTA OQ JÁ ESTÁ NA PASTA

from MODULOS import funcoes2 ##PASTA(MODULOS), IMPORTAR(funcao2)

from MODULOS.pessoa import idade,esporte ##DA PASTA(MODULOS), NO ARQUIVO(.variaveis), IMPORTAR ITENS ESPECÍFICOS(idade,esporte)

from cidade import * ##DO ARQUIVO(cidade) IMPORTE TUDO(*) | CUIDADO POIS IMPORTA TUDO (variáveis, funções e etc...)

#FUNÇÕES2 from MODULOS
nome=funcoes2.nomer
#FUNCOES
funcoes.saudacao(funcoes.nome)
#IDADE,ESPORTE from MODULOS.pessoa
print(f'UM PASSARINHO ME CONTOU QUE VC TEM {idade} anos')
print(f'VC GOSTA DE {esporte}')
#* from cidade
print(f'VC MORA EM {cidade} |CEP {cep} ')