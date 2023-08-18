from abc import ABC, abstractclassmethod

__all__ = [
    "Account",
    "CurrentAccount",
    "SavingsAccount",
]


class Account(ABC):
    def __init__(
        self, agency: int, account_number: int,
        balance: float = 0
    ) -> None:
        super().__init__()
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account_number!r}, {self.balance!r})'
        return f'{cls_name} {attrs}'

    @abstractclassmethod
    def withdrawal(self, withdrawal_amount: float): ...

    def deposit(self, deposit_amount: float) -> float:
        self.balance += deposit_amount
        print('DEPÓSITO')
        self.details(f'(DEPÓSITO {deposit_amount:,.2f})')
        return self.balance

    def details(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.balance:,.2f} {msg}\n----')


class SavingsAccount(Account):
    def withdrawal(self, withdrawal_amount):
        withdrawal_condition = self.balance - withdrawal_amount >= 0
        if withdrawal_condition:
            self.balance -= withdrawal_amount
            print('SALDO DISPONÍVEL')
            self.details(f'(SAQUE {withdrawal_amount:,.2f})')
            return self.balance

        print('SALDO INDISPONÍVEL')
        self.details(f'(SAQUE NEGADO {withdrawal_amount:,.2f})')
        return self.balance


class CurrentAccount(Account):
    def __init__(
        self, agency: int, account_number: int,
        balance: float = 0, limit: float = 0
    ) -> None:
        super().__init__(agency, account_number, balance)
        self.limit = limit

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account_number!r}, '\
                f'{self.balance!r}, {self.limit!r})'
        return f'{cls_name} {attrs}'

    def withdrawal(self, withdrawal_amount):
        withdrawal_condition = \
            self.balance - withdrawal_amount >= (-self.limit)
        if withdrawal_condition:
            self.balance -= withdrawal_amount
            print('SALDO DISPONÍVEL')
            self.details(
                f'(SAQUE {withdrawal_amount:,.2f}) '
                f'(LIMITE DE CREDITO {-self.limit:,.2f})'
            )
            return self.balance

        print('SALDO INDISPONÍVEL')
        self.details(
            f'(SAQUE NEGADO {withdrawal_amount:,.2f}) '
            f'(LIMITE DE CREDITO {-self.limit:,.2f})'
        )
        return self.balance


if __name__ == '__main__':
    savings_account1 = SavingsAccount(111, 222, 0)
    savings_account1.withdrawal(1)
    savings_account1.deposit(1)
    savings_account1.withdrawal(1)
    savings_account1.withdrawal(1)
    print('#####')
    current_account1 = CurrentAccount(111, 333, 0, 1)
    current_account1.withdrawal(1)
    current_account1.deposit(1)
    current_account1.withdrawal(1)
    current_account1.withdrawal(1)
    print('#####')
