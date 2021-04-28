from random import randint
sorteado = randint(0,10)
num = -1
palpite = 0
while num != sorteado:
    num = int(input('Adivinhe um número de 0 a 10: '))
    if num == sorteado:
        print('Voce acertou! o número sorteado é: {}'.format(sorteado))
        palpite += 1
    else:
        palpite += 1
        if num < sorteado:
            print('O número é mais alto')
        if num > sorteado:
            print('O número é mais baixo')
print('O numero de plpites foi: {}'.format(palpite))
print('Fim')