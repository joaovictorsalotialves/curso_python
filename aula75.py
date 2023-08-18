"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


fala_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom Noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(fala_bom_dia(nome))
    print(falar_boa_noite(nome))
