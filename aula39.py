"""
Iterando strings com while
"""

nome = 'João Victor'
novo_nome = ''

i = 0
while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1

novo_nome += '*'

print(novo_nome)
