##EXERCICIO 02
""" Crie uma pasta chamada meu_pacote
Dentro dela, crie:
formatador.py → função caixa_alta(texto) → retorna o texto em letras maiúsculas

numeros.py → função eh_par(numero) → retorna True se for par

No main.py:
Importe e use as funções do pacote
Exiba o resultado formatado """
#################################################################################
from meu_pacote import formatador, par
frase=input('DIGITE AQUI A FRASE PARA CAIXA ALTA:\n')
numero=int(input('DIGITE AQUI UM NÚMERO PARA VERIFICAÇÃO:\n'))

print(f'\nFRASE EM CAIXA ALTA: {formatador.caixa_alta(frase)}')
if par.eh_par(numero)==True:
    print(F'NÚMERO {numero} É PAR')
else:
    print(f'NÚMERO {numero} É IMPAR')