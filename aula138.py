# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = 1234

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('CLASSE CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'CPF aluno'


c1 = Cliente('João', 'Alves')
c1.falar_nome_classe()
print(c1.cpf)
a1 = Aluno('Vinicius', 'Alves')
a1.falar_nome_classe()
print(a1.cpf)

# help(Pessoa)
# help(Cliente)
# help(Aluno)
