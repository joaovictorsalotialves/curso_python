"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


# def verifica_numeros_duplicados(lista_inteiros):
#     set_inteiros_duplicados = set()
#     for numero in lista_inteiros:
#         if lista_inteiros.count(numero) > 1:
#             set_inteiros_duplicados.add(numero)

#     if len(set_inteiros_duplicados) == 0:
#         return -1

#     indice_primeira_duplicacao = 0
#     numero_retorno = 0
#     for i, numero_duplicado in enumerate(set_inteiros_duplicados):
#         count_aparicoes_numeros_duplicado = 0
#         for indice_atual, numero in enumerate(lista_inteiros):
#             if numero == numero_duplicado:
#                 count_aparicoes_numeros_duplicado += 1
#                 if count_aparicoes_numeros_duplicado == 2:
#                     if (not i) or (indice_primeira_duplicacao > indice_atual):
#                         indice_primeira_duplicacao = indice_atual
#                         numero_retorno = numero

#     return numero_retorno


def verifica_numeros_duplicados(lista_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_inteiros in lista_de_listas_de_inteiros:
    print(
        lista_inteiros,
        verifica_numeros_duplicados(lista_inteiros)
    )
