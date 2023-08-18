import sys

# Generator expression, Iterable e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(100)]
generator = (n for n in range(100))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
