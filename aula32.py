"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_str = input('Informe um número inteiro: ')

# try:
#     numero_int = int(numero_str)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {numero_int} é {par_impar_texto}')
# except:
#     print('Isso não é um número inteiros')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario_atual = input('Informe a hora do dia: ')

# try:
#     horario_atual_int = int(horario_atual)

#     if horario_atual_int <= 11:
#         print('Bom Dia!')
#     elif horario_atual_int <= 17:
#         print('Boa Tarde!')
#     elif horario_atual_int <= 23:
#         print('Boa Noite!')
#     else:
#         print('Informe um número apropriado para representar as horas')

# except:
#     print('Por favor, informe um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Informe seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
