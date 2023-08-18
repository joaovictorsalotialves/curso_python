# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper (self):
#         print('CHAMOU UPPER')
#         return super(MinhaString, self).upper()


# string = MinhaString('João')
# print(string.upper())


class A:
    atributo_a = 'valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor C'

    def __init__(self, *args, **kwargs):
        print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super(B, self).metodo()
        super(C, self).metodo()
        # A.metodo(self)
        # B.metodo(self)
        print('C')


# print('CLASSE C')
# print(*C.mro(), sep='\n')
# print('CLASSE B')
# print(*B.mro(), sep='\n')

c = C('atributo', 'Qualquer')

print(c.atributo)
print(c.outra_coisa)

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
