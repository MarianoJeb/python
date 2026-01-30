# Exercício 1 – Relógio de verificação
# Mostre a hora atual no terminal, mas com a seguinte regra:
# Se a hora for antes das 12h, imprima: "Bom dia!"
# Se estiver entre 12h e 18h: "Boa tarde!"
# Depois disso: "Boa noite!"

from datetime import datetime
agr=datetime.now()
if agr.hour<12: print(agr.strftime("⏱Horário:%H:%M\n🌻Bom dia!"))
elif agr.hour>=12 and agr.hour<18: print(agr.strftime("⏱Horário:%H:%M\n☕Boa tarde!"))
else: print(agr.strftime("⏱Horário:%H:%M\n😴Boa noite!"))