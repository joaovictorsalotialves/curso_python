# Crie um programa que tenha uma tupla de tuplas que contenha nomes de produtos e seus
# respectivos preços e, ao final exiba os produtos em formato tabular.
# Abaixo os dados para a criação da tupla:
# name     preço
# Tv       R$ 1200.00
# fone     R$ 85.00
# celular  R$ 2000.00
# caneca   R$ 25.00
# mouse    R$ 150.00

produtos = (
    ('TV', 1200),
    ('fone', 85),
    ('celular', 2000),
    ('caneca', 25),
    ('mouse', 150),
)

tamanho_nome = 0

print('=' * 40)
print('{:^40}'.format('Tabela de Produtos'))
print('=' * 40)
for produto in produtos:
    for i, dados in enumerate(produto):
        if len(produto) - 1 == i:
            espaco = 30 - tamanho_nome
            print(f'{dados:>7.2f}')
            break
        tamanho_nome = len(dados)
        print(f'{dados:.<30}R$ ', end='')
