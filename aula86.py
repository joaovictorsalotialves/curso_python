# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'João',
    'sobrenome': 'Alves',
}

# a, b = pessoa.keys()
# print(a)
# print(b)

# a, b = pessoa.values()
# print(a)
# print(b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)


def mostra_argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostra_argumentos_nomeados(nome='João', qlq=123)
mostra_argumentos_nomeados(**pessoas_completa)
