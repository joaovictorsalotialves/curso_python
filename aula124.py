class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def papar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')

        print(f'{self.nome} está parando de filmando...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.papar_filmar()
c1.fotografar()

print()

c2.papar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.papar_filmar()
c2.fotografar()
