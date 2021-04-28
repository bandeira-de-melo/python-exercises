'''for c in range(1, 10):
    print(c)
print('FIM!')'''
'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''
'''r ='S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar [S/N]?')).upper()
print('FIM')'''

n = 1
impar = par = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        if n != 0:
            par += 1
    else:
        impar += 1
print('Voce digitou {} números pares e {} números ímpares'.format(par, impar))

