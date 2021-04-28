num = int(input('Escolha um número para saber sua tabuada: '))
for c in range(0, 11):
    print('{} X {} = {}'.format(num, c, (num*c)))