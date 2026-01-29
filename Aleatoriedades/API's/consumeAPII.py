import requests
import streamlit

streamlit.title('MÚSIQUINHAS LEGAIS👍')

def search_music(banda:vars, musica:vars):
    endpoint=(f'https://api.lyrics.ovh/v1/{banda}/{musica}')
    response=requests.get(endpoint)
    return response.json()['lyrics'] if response.status_code==200 else ''


banda:str=streamlit.text_input('Digite o nome da banda: ', key='banda').strip()
musica:str=streamlit.text_input('Digite o nome da música: ', key='musica').strip()

BOTTON=streamlit.button('Pesquisar')
if BOTTON:
    lyrics=search_music(banda, musica)
    if lyrics:
        streamlit.success('Música encontrada!')
        streamlit.text(lyrics)
    else:
        streamlit.error("Música não encontrada\n):")
    