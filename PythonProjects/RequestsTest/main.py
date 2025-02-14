import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='4ce457196981f719057294894bb3d740'
HEADER ={'Content-Type': 'application/json', 'trainer_token':TOKEN}

body_create={
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER,json=body_create)
print(response_create.text)
if response_create.status_code == 201:
    data = response_create.json()
    id_value = data["id"]
    print(id_value)

body_izmenit={
    "pokemon_id": id_value,
    "name": "Регинча",
    "photo_id": 2
}
response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER,json=body_izmenit)
print(response_create.text)


body_poymat={
    "pokemon_id": id_value,
}

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,json=body_poymat)
print(response_create.text)


