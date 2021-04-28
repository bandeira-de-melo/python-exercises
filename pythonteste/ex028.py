import random
num = random.randrange(1, 6)
chute = int(input('Tente adivinhar o número de 1 a 5:'))
if num == chute:
    print('Parabéns voce a acertou o número é {}'.format(num))
else:
    print('Não foi dessa vez. Quem sabe na próxima?')
print('Tenha um ótimo dia!')
