# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'João Victor'
pessoa['sobrenome'] = 'Saloti Alves'

print(pessoa[chave])

pessoa[chave] = 'João'
del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
