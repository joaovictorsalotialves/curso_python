# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda', ]
tupla = 'Python', 'é', 'legal'

salas = [
    ['Maria', 'Helena', ],
    ['Elanine', ],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40), ],
]

# p, s, *_, ap, u = lista
# print(p, u, ap)

for nome in lista:
    print(nome, end=' ')

print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')
