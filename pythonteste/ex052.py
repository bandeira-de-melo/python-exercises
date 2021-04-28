num = int(input('Digite um numero para saber se ele é primo:'))
prim = 0
for c in range(1, num + 1):
    if num % c == 0:
        prim = prim + 1
if prim == 2:
    print('{} é um numero primo'.format(num))
else:
    print('{} não é um número primo'.format(num))