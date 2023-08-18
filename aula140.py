# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)
########### TESTE 1 ###########
# class O:
#     ...

#     # 10
#     def quem_sou(self):
#         print('O')

# class A(O):
#     ...

#     # 3
#     # def quem_sou(self):
#     #     print('A')

# class B(O):
#     ...

#     # 5
#     # def quem_sou(self):
#     #     print('B')

# class C(O):
#     ...

#     # 7
#     # def quem_sou(self):
#     #     print('C')

# class D(O):
#     ...

#     # 8
#     # def quem_sou(self):
#     #     print('D')

# class E(O):
#     ...

#     # 9
#     # def quem_sou(self):
#     #     print('E')

# class K1(A, B, C):
#     ...

#     # 2
#     # def quem_sou(self):
#     #     print('K1')

# class K2(B, C, D):
#     ...

#     # 4
#     # def quem_sou(self):
#     #     print('K2')

# class K3(C, D, E):
#     ...

#     # 6
#     # def quem_sou(self):
#     #     print('K3')

# class Z(K1, K2, K3):
#     ...

#     # 1
#     # def quem_sou(self):
#     #     print('Z')

# z = Z()
# z.quem_sou()

########### TESTE 2 ###########

class O:
    ...

    # 14
    # def quem_sou(self):
    #     print('O')


class A1(O):
    ...

    # 3
    # def quem_sou(self):
    #     print('A1')


class A2(O):
    ...

    # 4
    # def quem_sou(self):
    #     print('A2')


class A3(O):
    ...

    # 5
    # def quem_sou(self):
    #     print('A3')


class B1(O):
    ...

    # 7
    # def quem_sou(self):
    #     print('B1')


class B2(O):
    ...

    # 8
    # def quem_sou(self):
    #     print('B2')


class B3(O):
    ...

    # 9
    # def quem_sou(self):
    #     print('B3')


class C1(O):
    ...

    # 11
    # def quem_sou(self):
    #     print('C1')


class C2(O):
    ...

    # 12
    # def quem_sou(self):
    #     print('C2')


class C3(O):
    ...

    # 13
    # def quem_sou(self):
    #     print('C3')


class K1(A1, A2, A3):
    ...

    # 2
    # def quem_sou(self):
    #     print('K1')


class K2(B1, B2, B3):
    ...

    # 6
    # def quem_sou(self):
    #     print('K2')


class K3(C1, C2, C3):
    ...

    # 10
    # def quem_sou(self):
    #     print('K3')


class Z(K1, K2, K3):
    ...

    # 1
    # def quem_sou(self):
    #     print('Z')


z = Z()
# z.quem_sou()
print(Z.mro())
