import os

palavra = 'chocolate'
acertos = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        acertos += letra

    palavraFormada = ''
    for letraSecreta in palavra:
        if letraSecreta in acertos:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'

    print('Palavra formada:', palavraFormada)

    if palavraFormada == palavra:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra)
        print('Tentativas:', tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
