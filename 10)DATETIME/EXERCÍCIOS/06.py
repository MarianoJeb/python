# Peça ao usuário para informar a data de fabricação de um produto.
# Considere que ele vence em 180 dias.
# Mostre: 
# A data de validade
# Se o produto ainda está válido ou já venceu
# Quantos dias faltam ou há quanto tempo passou do prazo
from datetime import datetime, timedelta


def calc_validade(data_fabricacao:datetime, dia_validade:int):
    hoje=(datetime.today()).date()
    dia_data=timedelta(days=dia_validade)
    data_vencimento=(data_fabricacao+dia_data).date()
    data_analise=(data_vencimento-hoje)
    
    if data_analise.days>0:
        print(f"Faltam ainda {data_analise.days} dias para sue produto sair da validade!\nO seu produto irá vencer dia {data_vencimento}")
    elif data_analise.days<0:
        print(f"Produto vencido desde: {data_vencimento}\nJá fazem {data_analise.days*-1} dias que estragou!")
    elif data_analise.days==0: 
        print(f"O produto estragou hoje!\n):")



while True:
    try:
        print("\n--Testando Validade--\n1-Conferir validade\n2-Sair")
        key=int(input("->"))
        if key==1:
            fabricacao=input("Digite a data de fabricação:\n->")
            data_fabricacao=datetime.strptime(fabricacao, "%d/%m/%Y")
            dias=int(input("Tempo de validade em dias:\n->"))
            calc_validade(data_fabricacao, dias)
        elif key==2:break
        else: raise ValueError
    except ValueError:
        print("Argumento inválido, tente novamente")