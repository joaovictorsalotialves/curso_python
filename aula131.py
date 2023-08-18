# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.corTinta = cor
        self.corTampa = cor

    @property
    def cor_tinta(self):
        print('PROPERTY')
        return f'Cor Tinta: {self.corTinta}'

    @property
    def cor_tampa(self):
        print('PROPERTY')
        return f'Cor Tampa: {self.corTampa}'

    # def get_cor(self):
    #     print('GET COR')
    #     return self.cor


caneta = Caneta('Azul')
print(caneta.cor_tinta)
print(caneta.cor_tampa)

# print(caneta.get_cor())
