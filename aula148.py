# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instancia')
        return super().__new__(cls)

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return f'{self.__class__.__name__}()'


a = A(1)
print(a)
