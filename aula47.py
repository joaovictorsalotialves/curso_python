"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

PALAVRA_SECRETA = 'palmeiras'
letras_acertadas = ''
letras_digitadas = ''

while True:
    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if len(letra_digitada) == 0:
        print('Digite alguma letra')
        continue

    if letra_digitada in letras_digitadas:
        print(
            f'A letra "{letra_digitada}" já foi digitada. '
            'Por favor, informe outra letra'
        )
        continue

    letras_digitadas += letra_digitada

    if (letra_digitada in PALAVRA_SECRETA) and \
            (letra_digitada not in letras_acertadas):
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_palavra_secreta in PALAVRA_SECRETA:
        if letra_palavra_secreta in letras_acertadas:
            palavra_formada += letra_palavra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == PALAVRA_SECRETA:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', PALAVRA_SECRETA)
        print('Tentativas:', len(letras_digitadas))

        # Resetar o jogo para comecar denovo
        letras_acertadas = ''
        letras_digitadas = ''
