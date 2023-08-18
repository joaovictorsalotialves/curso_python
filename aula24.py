# Operadores in e not in
# Strings são iteráveis

nome = 'João Victor'
# print(nome[2])
# print(nome[-4])

# print('ã' in nome)
# print('z' in nome)
# print('Vic' in nome)
# print(10 * '-')
# print('ã' not in nome)
# print('z' not in nome)
# print('Vic' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
