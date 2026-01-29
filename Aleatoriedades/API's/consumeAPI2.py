##How to conusme an API 2-Lan Code
import requests

url:str=('https://economia.awesomeapi.com.br/last/')
moeda:str='USD-BRL'

def moeda_calc(moeda)->dict:
    response=requests.get(f'{url}{moeda}')
    moeda_data=response.json()
    return moeda_data

USD=moeda_calc(moeda)
venda=(USD['USDBRL']['bid'])
compra=(USD['USDBRL']['ask'])
print(f'-------{USD["USDBRL"]['name']}-------\nCOMPRA:{compra}\nVENDA:{venda}')