# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum


class Foo:
    ...


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


# Direcaoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

# print(Direcaoes(1), Direcaoes['ESQUERDA'], Direcaoes.ESQUERDA)
# print(Direcaoes(1).name, Direcaoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ABAIXO)
mover(Direcoes.ACIMA)

print(type(enum.Enum))
print(type(Direcoes))
print(type(Foo))
