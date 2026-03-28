from datetime import datetime

now=datetime.now()
nowstr=now.strftime(r"%d/%m/%Y, %H:%M")
with open("EXERCICIO/01/relatorio.txt", mode='w', encoding='utf-8') as arquivo:
    arquivo.write(f"Estou aprendendo Python!\n{nowstr}")