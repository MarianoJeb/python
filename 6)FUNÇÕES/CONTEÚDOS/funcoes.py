def saudacao():
    print("Olá, que bom te conhecer!!")

def saudacao_nome(nome):  #entre () é o parâmetro
    print(f"Nossa, que prazer te conhecer {nome}!!")

saudacao_nome("Pedro") # aqui entre () é o argumento


""" def somar(num1,num2):
    result=num1+num2
    print(f"{num1}+{num2}={result}")

somar(3,19) """

def somar(num1,num2):
    result=num1+num2
    return result #retorna o valor, fazendo possivel por em variavel

resultado=somar(3,19) 
print(resultado)
print(somar(10,10))

def desconto(preco,perc):
    preco_desconto=preco/100*perc
    return preco_desconto

def preco_final(preco,perc):
    pd=preco*(perc/100)
    pf=preco-pd
    return pf
descontado=desconto(300,45)
final_price=preco_final(300,45)
print(f"Valor total do desconto:{descontado}\nPreço final:{final_price}")