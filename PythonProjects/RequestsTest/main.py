import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='4ce457196981f719057294894bb3d740'
HEADER ={'Content-Type': 'application/json', 'trainer_token':TOKEN}
body_create={
    "name": "Бульбазавр",
    "photo_id": 1
}
body_izmenit={
    "pokemon_id": "233690",
    "name": "Регинча",
    "photo_id": 2
}
body_poymat={
    "pokemon_id": "233690"
}
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER,json=body_create)
print(response_create.text)'''

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER,json=body_izmenit)
print(response_create.text)

'''response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,json=body_poymat)
print(response_create.text)'''