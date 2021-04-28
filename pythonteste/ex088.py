from random import randrange
from time import sleep
sorteioGeral = []
sorteioTemp = []
numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
for l in range(numJogos):
    for c in range(0, 6):
        numb = randrange(1, 61)
        if numb in sorteioTemp:
            numb = randrange(1, 61)
        sorteioTemp.append(numb)
    sorteioTemp.sort()
    sorteioGeral.append(sorteioTemp[:])
    sorteioTemp.clear()
print('-=' * 30)
for l in range(len(sorteioGeral)):
    print(f'Jogo: {l + 1} {sorteioGeral[l]}')
    sleep(1)





