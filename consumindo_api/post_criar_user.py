from pprint import pprint

import requests

print = pprint

url = 'http://127.0.0.1:3001/users'

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
    print(response.json())
    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
