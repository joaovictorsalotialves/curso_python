# Classes decoradoras (Decorator classes)
class Multiplicar:
    # def __init__(self, func):
    #     self.func = func
    #     self._multiplicador = 10

    # def __call__(self, *args, **kwargs):
    #     resultados = self.func(*args, *kwargs)
    #     return resultados * self._multiplicador

    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def multiplica_soma(*args, **kwargs):
            resultados = func(*args, **kwargs)
            return resultados * self._multiplicador
        return multiplica_soma


@Multiplicar(10)
def soma(x, y):
    return x + y


dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
