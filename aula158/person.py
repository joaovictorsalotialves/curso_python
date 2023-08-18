import account

__all__ = [
    "Person",
    "Client",
]


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._idade = age

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{cls_name} {attrs}'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> str:
        self._name = name
        return self._name

    @property
    def age(self) -> int:
        return self._idade

    @age.setter
    def age(self, age: int) -> int:
        self._idade = age
        return self._idade


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: account.Account | None = None


if __name__ == '__main__':
    c1 = Client('João', 17)
    c1.account = account.CurrentAccount(111, 222, 0, 0)
    print(c1)
    print(c1.account)
    c2 = Client('Vinicius', 17)
    c2.account = account.SavingsAccount(112, 223, 100)
    print(c2)
    print(c2.account)
