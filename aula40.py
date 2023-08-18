"""Calculadora com while"""
OPERADORES_PERMITIDOS = '+-*/'

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-*/): ')

    numeros_validos = None
    num_1_float = 0.0
    num_2_float = 0.0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if operador not in OPERADORES_PERMITIDOS:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')

    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float
    elif operador == '/':
        try:
            resultado = num_1_float / num_2_float
        except:
            print('Não é possível realizar a divisão por ZERO')
            continue
    else:
        print('ERRO INESPERADO!')

    print(f'{numero_1} {operador} {numero_2} = {resultado}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
