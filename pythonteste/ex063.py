'''num = int(input('Quantos elementos de uma sequencia de Fibonacci você deseja ver? '))
n = 0
n2 = 1
t = 0
cont = 3
while cont <= num:
    t = n  + n2
    n = n2
    n2 = t
    cont += 1
    if t == 1:
        print(0, end=' ')
        print(1, end=' ')
    print(t, end=' ')'''

# Código Guanabara
n = int(input('Qual o número de termos que voce quer ver? '))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')