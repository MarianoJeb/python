import requests
import streamlit

url_base='https://viacep.com.br/ws/'

def cepper(cep:str)->dict:
    if len(str(cep))!=8:
        return ''
    cep_url=f'{url_base}{cep}/json/'
    responce=requests.get(cep_url)
    data=responce.json()
    return data if responce.status_code==200 else ''

def view_infos(cep):
    streamlit.title('INFORMAÇÕES',)
    streamlit.text(f'CEP:{cep['cep']}')
    streamlit.text(f'BAIRRO:{cep['bairro']}')
    streamlit.text(f'CIDADE:{cep['localidade']}')
    streamlit.text(f'ESTADO:{cep['estado']}')

streamlit.title('PROCURADOR DE CEP', text_alignment='center')
input_cep=streamlit.text_input('DIGITE AQUI SEU CEP:', key="CEP", placeholder='Digite aqui o seu cep...')
BUTTON=streamlit.button('PROUCURAR')

if BUTTON:
    cep=cepper(input_cep)
    if cep:
        streamlit.success('CEP ENCONTRADO', icon='🚗', width=200)
        view_infos(cep)
    else:
        streamlit.error('CEP NÃO IDENTIFICADO')