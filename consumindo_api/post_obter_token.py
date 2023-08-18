from pathlib import Path
from pprint import pprint

import requests

CAMINHO_TOKEN = Path(__file__).parent / 'token.txt'

print = pprint

url = 'http://127.0.0.1:3001/tokens'

user_data = {
    "password": "123456",
    "email": "jsalotialves@gmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)

    response_data = response.json()
    token = response_data['token']

    with open(CAMINHO_TOKEN, 'w') as file:
        file.write(token)

    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
