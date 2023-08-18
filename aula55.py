"""
Introdução ao desempacotamento
"""
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2, _)

_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz']
print(nome3, _)
