# Try, except, else, finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# a = 18
# b = 0
# c = a / b

# try:
#     a = 18
#     b = 0
#     print('Linha 1'[111])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError:
#     print('Dividiu por zero.')
# except NameError:
#     print('Nome não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG: ', error)
#     print('Nome: ', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')

# print('CONTINUAR')

try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
