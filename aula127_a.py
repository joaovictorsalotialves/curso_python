# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


def fazer_dump(db, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(db, arquivo, indent=2)


p1 = Pessoa('João', 17)
p2 = Pessoa('Vinicius', 21)
db = [vars(p1), vars(p2)]

if __name__ == '__main__':
    fazer_dump(db, CAMINHO_ARQUIVO)
