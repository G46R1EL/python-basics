# Jogo para adivinhar qual é a palavra secreta

import random

print('Este é um jogo de adivinhação. Tente descobrir a palavra oculta.')

lista_palavras_possiveis = ['python', 'hardware', 'computador', 'javascript', 'tecnologia', 'internet' ]

palavra_secreta = random.choice(lista_palavras_possiveis)

letras_acertadas = ''

while True:

    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Valor Inválido. Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada


    palavra_formada = ''
    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += '*'
    print(f'Sua tentativa: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('Parabéns!!! Você descobriu a palavra!')
        break
