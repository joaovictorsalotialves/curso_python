"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""

nome = 'João'
preco = 1000.9484939
variavel = '%s, o preco é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04X' % (15, 15))
