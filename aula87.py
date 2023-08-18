# List Comprehension em Python
# List Comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)


# Mapeamento de dados em list comprehesion
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')
# p(novos_produtos)

lista = [n for n in range(10) if n < 5]
# p(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
# p(novos_produtos)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
lista = [
    [y for y in range(3)]
    for x in range(3)
]
print(lista)

# Exemplo da aula do YouTube
string = 'João Victor Saloti Alves'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])
print(nova_string)

# flat
numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)
