##EXERCICIO 05:
""" Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:
O valor da compra deve ser maior ou igual a 100
E o cliente precisa estar cadastrado no programa de fidelidade
Se as duas condições forem verdadeiras, mostre: Frete grátis aplicado!
Caso contrário: Frete não disponível gratuitamente. """
print("FRETE GRÁTIS:")
valor=float(input("Digite o valor total da compra:\n"))
PF=input("Você é cadastrado no programa de fidelidade? \n(S/N)\n").lower()
if valor>=100 and (PF=="s" or PF=="sim"):
    print("FRETE GRÁTIS APLICADO!!\n(:)")
else:
    print("FRETE GRÁTIS NÃO DISPONÍVEL!!\n):")

#OBSERVAÇÕES:
#.LOWWER() transforma tudo em minúsculo
#.UPPER() transforma tudo em maiúsculo13