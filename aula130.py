# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_passaword(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        return f'LOG: {msg}'


# c1 = Connection()
# c1.set_user('João')
# c1.set_passaword('123')

c1 = Connection.create_with_auth('João', '123')

print(c1.user)
print(c1.password)
print(c1.log('Mensagem de log'))
