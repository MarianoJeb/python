from datetime import datetime

agora=datetime.now()
# print(f'DIA:{agora.day}\nMÊS:{agora.month}\nANO:{agora.year}')
# print(f'HORA:{agora.hour}\nMINUTOS:{agora.minute}\nSEGUNDO:{agora.second}')

aniversario=datetime(year=2012, month=3, day=3) ##N precisa dos kw (:
print (aniversario)
print(aniversario.strftime("Meu aniversário é dia %d/%m/%Y"))

print(agora.strftime("Hoje é dia %d do mês %m do ano %Y🗓️")) #y=ano abreviado | Y=ano completo
print(agora.strftime("Agora são %H horas, %M minutos e %S segundos⏱️"))

#OBS strftime: Mês em letras: %b(abreviado) | %B(extenso)
                #dia da semana: %a(abreviado) | %A(extenso)
                #data e hora formatados: %c (Complete)
                #data representation local: %x
                #hora representation local: %X


data_str="31/08/2026" ##Converte uma string em um objeto abreviado.
data_convertida=datetime.strptime(data_str, "%d/%m/%Y")

#OBS strptime: ordem dos parâmetros=(*Oq vai ser convertido, *Ordem)
