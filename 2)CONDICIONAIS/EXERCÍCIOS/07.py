#EXERCICIO 7:
""" Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:
"carro" → "Veículo terrestre"

"bicicleta" → "Transporte sustentável"

"avião" ou "helicóptero" → "Transporte aéreo"

Qualquer outro → "Transporte desconhecido" """

transporte=input("digite um meio de transporte;\n").lower()

match transporte:
    case "carro":
        print("VEIVULO TERRESTRE")
    case "bicicleta":
        print("TRANSPORTE SUSTENTÁVEL")
    case "avião" | "aviao" | "helicoptero" | 'helicóptero' :
        print("TRANSPORTE AÉREO")
    case "navio" | "barco":
        print("TRANSPORTE AQUÁTICO")
    case _:
        print("TRANSPORTE DESCONHECIDO")
#OBSERVAÇÕES:
#.LOWWER() transforma tudo em minúsculo
#.UPPER() transforma tudo em maiúsculo
#operador | significa "ou" dentro do match case
#case _ é o para caso padrão (else)
