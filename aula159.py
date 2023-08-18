# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass, field, fields


@dataclass
class Pessoa:
    nome: str
    sobrenome: str = field(
        default='Not sed',
        repr=False
    )
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)

    # def __init__(self, nome, sobrenome) -> None:
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     print('PÓS init')
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('João', 'Alves')
    # p2 = Pessoa('João', 'Alves')
    # print(p1)
    # print(p2)
    # print(p1 == p2)
    # print(p1.nome_completo)
    # p1.nome_completo = 'João Victor Saloti Alves'
    # print(p1.nome_completo)

    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True)
    # print(ordenadas)

    print(asdict(p1))
    print(astuple(p1))

    print(fields(p1))

    # print(type(Pessoa))
