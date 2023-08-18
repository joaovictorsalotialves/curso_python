from pathlib import Path

import requests

url = 'http://localhost:3001/images/1674246624259_18912.jpg'
nome_arquivo = str(Path(__file__).parent / url.split('/')[-1])

response = requests.get(url=url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)

else:
    # Erros
    print(response.status_code)
    print(response.reason)
