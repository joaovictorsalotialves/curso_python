# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


# Função para criar outras funções
def criar_multiplicador(multiplicador):
    def multiplicar(multiplicando):
        return multiplicando * multiplicador
    return multiplicar


# Criando as funções
f_duplicar = criar_multiplicador(2)
f_triplicar = criar_multiplicador(3)
f_quadruplicar = criar_multiplicador(4)

print(f_duplicar(12))
print(f_triplicar(12))
print(f_quadruplicar(12))
