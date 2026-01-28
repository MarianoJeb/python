idade=20
if idade<=18:
    print("Vc é menor de idade!!")
else:
    print("Vc é maior de idade!!")

################################################
numero = float(input("Digite um número:\n"))
if numero%2==0:
    print ("O número é par!!")
else:
    print("O número é impar!!")

################################################

nota=int(input("Digite sua nota de 0 a 100:\n"))
if nota>=90:
    print("A")
elif nota>=80:
    print("B")
elif nota>=70:
    print("C")
elif nota>=60:
    print("D")
else:
    print("F")

################################################

tem_carteira=True
if idade>=18:
    print("Você tem idade para dirigir!!")
    if tem_carteira:
        print("Você pode dirigir!!")
    else:
        print("VocÊ não pode dirigir sem carteira!!")
else:
    print("Você não tem idade para dirigir!!")

################################################

animal_favorito=input("Qual o seu animal favorito?\n").lower()
if animal_favorito=="gato" or animal_favorito=="cachorro": ##operador or (ou)
    print("você é mt legal!!!")
else:
    print("Vc tem um gosto peculiar!!")

################################################

if idade >=13 and idade <=19: ##operador and (e)
    print("Você é um adolescente!!")

################################################

chuva=True
if not chuva:  ##operador not (não)
    print("Hj não vai chover!!")
else:
    print("Hj vai chover!!")

##OBSERVAÇÕES:

#OR==ou(acrescenta mais opções)
#and==e(se isso e aquilo)
#not==não(inverte o valo booleano)