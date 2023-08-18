# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

from aula127_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    db = json.load(arquivo)
    p1 = Pessoa(**db[0])
    p2 = Pessoa(**db[1])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
