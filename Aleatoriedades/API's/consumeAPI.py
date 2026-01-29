##HOW TO CONNECT TO AN API USING PYTHON
import requests as rq

base_url='https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"

    response=rq.get(url) ##RESPOSTA(200,404,400) & INFORMAÇÕES
    if response.status_code==200:  ##.status_code VÊ O NÚMERO DA RESPOSTA
        pokemon_data=response.json() ##.json CONVERTE PARA TIPO UM DICIONÁRIO
        return pokemon_data
    else:
        print(f'Failed to retrive data\nERRO {response.status_code}')

pokemon_name='bulbasaur'
pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f'Name:{pokemon_info['name'].capitalize()}')
    print(f'ID:{pokemon_info['id']}')
    print(f'Height:{pokemon_info['height']}')
    print(f'Weight:{pokemon_info['weight']}')