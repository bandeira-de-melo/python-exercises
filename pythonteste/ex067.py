n = 0
q = 1
mult = n * q
while True:
    n = int(input('Digite um número pra saber a sua tabuada: '))
    if n < 0:
        break
    while q <= 10:
        print(f'{n} x {q} = {n * q}')
        q += 1
    q = 0
print('Acabou.')
