from pathlib import Path
from pprint import pprint

import requests
from get_token import token

CAMINHO_TOKEN = Path(__file__).parent / 'token.txt'

print = pprint

url = 'http://127.0.0.1:3001/alunos/2'

headers = {
    'Authorization': token
}

response = requests.delete(url=url, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)

    response_data = response.json()
    print(response_data)

    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
