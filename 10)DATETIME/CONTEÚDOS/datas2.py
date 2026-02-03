from datetime import datetime, timedelta

#timedelta->fzr cálculos com o tempo

hoje=datetime.now()
# umDia=timedelta(days=1)

# amanha=(hoje+umDia)
# print(amanha)

##Comparando datas:
# prazo=datetime(day=31, month=8, year=2026)
# if hoje>prazo:
#     print("Prazo vencido!")

futuro=datetime(day=3, month=3, year=2026)
dias_restantes=futuro-hoje
print(dias_restantes.days)


aniversario=datetime(day=4, month=11, year=(datetime.now()).year)

if aniversario.day == hoje.day and aniversario.month==hoje.month:
    print("Feliz anievrsário!")
elif aniversario > hoje:
    print ("Seu niver ainda vai acontecer!")
elif aniversario < hoje:
    print("Seu niver já passou!")
