from operator import itemgetter
names = {'nome1': 'Ana', 'nome2': 'Vanessa', 'nome3': 'Bruna'}
nomesOrdem = sorted(names.items(), key=itemgetter(1))
for i, v in enumerate(nomesOrdem):
    print(f'O {i+1}o nome em ordem alfabética é: {v[1]}')



