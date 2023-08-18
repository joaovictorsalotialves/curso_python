from pathlib import Path

CAMINHO_TOKEN = Path(__file__).parent / 'token.txt'

token = 'Bearer '

with open(CAMINHO_TOKEN, 'r') as file:
    token += file.read()
