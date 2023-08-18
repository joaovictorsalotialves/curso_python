"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    opcao = input(
        'Selecione uma opção\n'
        '[i]nserir  [a]pagar  [l]istar: '
    ).lower()

    if len(opcao) > 1:
        print('Por favor! Digite apenas a inicial da operação desejada')
        continue

    if not opcao.startswith(('i', 'a', 'l')):
        print('Por favor! Digite a inicial da opeação desejada')
        continue

    # INSERIR ITENS
    if opcao == 'i':
        os.system('cls')
        item_adicionado = input('Valor: ').lower()
        lista.append(item_adicionado)
    # APAGAR ITENS
    elif opcao == 'a':
        indice = input('Escolha o indice para apagar: ')
        try:
            del lista[int(indice)]
        except:
            print('Não foi possível apagar esse indice')
    # LISTAR ITENS
    elif opcao == 'l':
        os.system('cls')
        if lista:
            for i, item in enumerate(lista):
                print(f'{i} {item}')
        else:
            print('Nada para listar')
    else:
        print('ERRO INESPERADO! TENTE NOVAMENTE')
