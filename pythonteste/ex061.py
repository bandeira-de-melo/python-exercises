'''num = int(input('Digite um o primeiro valor da P.A: '))
rz = int(input('Digite a razão da pa: '))
lim = 10
elem = 0
print('Os {} primeiros elementos da P.A são: '.format(lim), end='')
while elem < lim:
    print(num, end='')
    print((' + ' if elem < 9 else ''), end='')
    num = num + rz
    elem += 1'''
primeiro = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razão
    cont += 1
print('FIM.')

