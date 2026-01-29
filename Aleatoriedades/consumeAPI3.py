##HOW TO CONNECT TO AN API USING PYTHON

import requests

url_base='https://viacep.com.br/ws/'

def cepper(cep:str)->dict:
    if len(str(cep))!=8:
        return 'O CEP DIGITADO NÃO EXISTE'
    cep_url=f'{url_base}{cep}/json/'
    responce=requests.get(cep_url)
    data=responce.json()
    return data if responce.status_code==200 else f'ERRO: {responce.status_code}'

def view_infos(cep):
    print('----INFORMAÇÕES----')
    print(f'CEP:{cep['cep']}')
    print(f'BAIRRO:{cep['bairro']}')
    print(f'CIDADE:{cep['localidade']}')
    print(f'ESTADO:{cep['estado']}')

input_cep=input('DIGITE AQUI SEU CEP:')

cep=cepper(input_cep)
view_infos(cep)