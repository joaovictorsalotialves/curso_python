a = 'AAAAA'
b = 'BBBBB'
c = 1.1
# string = 'b={1} a={0} a={0} b={1} c={2:.2f}'
# formato = string.format(a, b, c)

string = 'b={nome2} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
