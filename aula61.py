"""
Lista de listas e seus índices
"""
salas = [
    ['Maria', 'Helena', ],
    ['Elanine', ],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40), ],
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
