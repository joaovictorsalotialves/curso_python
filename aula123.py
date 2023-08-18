# Escopo da classe e de métodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args):
        return self.comendo(*args)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('maçã'))
print(leao.executar('maçã'))
