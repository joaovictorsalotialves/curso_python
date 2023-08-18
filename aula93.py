# Introduçao ás Generator functions em python
def generator(n=0, maximum=10):
    # yield 1
    # print('Continuando...')
    # yield 2
    # print('Mais uma...')
    # yield 3
    # print('Vou terminar')
    # return 'ACABOU'
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator()
for n in gen:
    print(n)

# Yield from


def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    if gen is not None:
        yield from gen()
    print('COMEÇOU GEN2')
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
for numero in g3:
    print(numero)
