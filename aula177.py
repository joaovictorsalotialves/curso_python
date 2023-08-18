# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

string_json = {
    'budget': None,
    'characters': ['Frodo',
                   'Sam',
                   'Gandalf',
                   'Legolas',
                   'Boromir'],
    'imdb_rating': 8.8,
    'is_movie': True,
    'original_title': 'The Lord of the '
    'Rings: The '
    'Fellowship of the '
    'Ring',
    'title': 'O Senhor dos Anéis: A '
    'Sociedade do Anel',
    'year': 2001
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(string_json, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
