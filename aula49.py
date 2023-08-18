"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, ...
Create  Read  Update  Delete (CRUD)
"""

lista = [10, 20, 30, 40]
# print(lista)
# lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)
lista.append(50)
print(lista)
lista.pop()
print(lista)
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(f'{lista} Removido, {ultimo_valor}')
