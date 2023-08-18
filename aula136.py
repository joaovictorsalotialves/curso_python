# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_enderecos_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO: ', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO: ', self.rua, self.numero)


cliente1 = Cliente('João')
cliente1.inserir_enderecos('Rua A', 1)
cliente1.inserir_enderecos('Rua B', 2)
endereco_externo = Endereco('Rua C', 3)
cliente1.inserir_enderecos_externo(endereco_externo)
cliente1.listar_endereco()

del cliente1

print('#####  Fim Código  #####')
