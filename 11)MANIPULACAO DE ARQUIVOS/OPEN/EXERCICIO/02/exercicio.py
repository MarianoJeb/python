letras=0
with open("EXERCICIO/02/arquivo.txt", mode="r", encoding='utf-8') as msg:
    mensagem=msg.read()
    letras=len(mensagem)

print(f"LETRAS TOTAIS: {letras}")