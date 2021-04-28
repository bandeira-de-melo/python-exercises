from time import sleep
from operator import itemgetter
from random import randint
sorteio = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
for k, v in sorteio.items():
    print(f'O {k} tirou o número {v}')
print('-'*30)
print('-'*30)
númerosOrdem = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(númerosOrdem):
    print(f'{i+1}o lugar {v[0]} com: {v[1]} ')
    sleep(1)