# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    if len(letra) == 1:
        letras.add(letra.lower())

    print(letras)
