# ----- TIPAGEM DE VARIAVEIS -----
# uma_string: str = 'Um valor'
# um_inteiro: int = 123456
# um_float: float = 1.23
# um_boolean: bool = True
# um_set: set = {1, 2, 3}  # mais sobre a seguir
# uma_lista: list = []  # mais sobre a seguir
# uma_tupla: tuple = 1, 2, 3  # mais sobre a seguir
# um_dicionario: dict = {}  # mais sobre a seguir


# ----- TIPAGEM DE FUNÇÕES -----
# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z


# ----- TIPAGEM DE LISTAS -----
# lista_inteiros: list[int] = [1, 2, 3, 4]
# lista_strings: list[str] = ['a', 'b', 'c', 'd']
# lista_tuplas: list[tuple] = [(1, 'a'), (2, 'b')]
# lista_listas_int: list[list[int]] = [[1], [4, 5]]


# ----- TIPAGEM DE DICIONARIOS -----
# um_dict: dict[str, int] = {
#     "A": 0,
#     "B": 0,
#     "C": 0,
# }
# um_dict_de_listas: dict[str, list[int]] = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
# }


# ----- TIPAGEM DE SETs -----
# um_set_de_inteiros: set[int] = {1, 2, 3}


# ----- TYPE ALIAS -----
# ListaInteiros = list[int]
# DictListaInteiros = dict[str, ListaInteiros]

# um_dict_de_listas: dict[str, list[int]] = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
# }


# ----- TYPE UNION -----
# string_e_inteiro: str | int = 1
# string_e_inteiro = "A"
# string_e_inteiro = 2
# lista: list[int | str] = [1, 2, 3, 'a']


# ----- OPTIONAL TYPING -----
# def soma(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int):
#         return x + y
#     return x + x


# ----- CALLABLE -----
# from collections.abc import Callable

# SomaInteiro = Callable[[int, int], int]


# def executa(func: SomaInteiro, a: int, b: int) -> int:
#     return func(a, b)


# def soma(a: int, b: int) -> int:
#     return a + b


# executa(soma, 1, 2)


# ----- TYPEVARS (TIPO DINAMICO) -----
# from typing import TypeVar

# T = TypeVar('T')


# def get_item(list: list[T], index: int) -> T:
#     return list[index]


# list_int = get_item([1, 2, 3], 1)  # int
# list_str = get_item(['a', 'b', 'c'], 1)  # str


# ----- CLASSES -----
# class Person:
#     def __init__(self, firstname, lastname) -> None:
#         self.firstname = firstname
#         self.lastname = lastname

#     @property
#     def full_name(self) -> str:
#         return f'{self.firstname} {self.lastname}'


# def say_my_name(person: Person) -> str:
#     return person.full_name


# ----- TIPO ANY -----
# from typing import Any

# any: Any = 'Qualquer tipo'
