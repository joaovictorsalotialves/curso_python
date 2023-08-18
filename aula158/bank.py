import account
import person

__all__ = [
    "Bank",
]


class Bank:
    def __init__(
        self, agencys: list[int] | None = None,
        clients: list[person.Client] | None = None,
        accounts: list[account.Account] | None = None
    ) -> None:
        self.agencys = agencys or []
        self.clients = clients or []
        self.accounts = accounts or []

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = f'({self.agencys!r}, {self.clients!r}, {self.accounts!r})'
        return f'{cls_name} {attrs}'

    def _check_agency(self, account: account.Account) -> bool:
        if account.agency in self.agencys:
            return True
        return False

    def _check_client(self, client: person.Client) -> bool:
        if client in self.clients:
            return True
        return False

    def _check_account(self, account: account.Account) -> bool:
        if account in self.accounts:
            return True
        return False

    @staticmethod
    def _check_account_is_client(
        client: person.Client, account: account.Account
    ) -> bool:
        if client.account is account:
            return True
        return False

    def auth(self, client, account) -> bool:
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_account_is_client(client, account)


if __name__ == "__main__":
    # Agencias
    agencys = [111, 222]
    # Clientes
    client1 = person.Client('João', 17)
    client2 = person.Client('Vinicius', 21)
    clients = [client1, client2]
    # Contas
    savings_account1 = account.SavingsAccount(111, 222, 0)
    current_account1 = account.CurrentAccount(222, 333, 0, 1)
    accounts = [savings_account1, current_account1]
    # Atribuindo Conta ao Cliente
    client1.account = savings_account1
    client2.account = current_account1
    # Banco
    bank1 = Bank(agencys, clients, accounts)

    # if bank1.auth(client1, savings_account1):
    #     client1.account.withdrawal(1)
    #     client1.account.deposit(1)
    #     client1.account.withdrawal(1)
    #     client1.account.withdrawal(1)

    #     client2.account.withdrawal(1)
    #     client2.account.deposit(1)
    #     client2.account.withdrawal(1)
    #     client2.account.withdrawal(1)
