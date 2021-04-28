'''num = int(input('Digite um número para calcular o seu fatorial: '))
num1 = num - 1
resul = num * num1
while num1 > 1:
    num1 = num1 - 1
    resul = resul * num1
print('O fatorial de {} é: {}'.format(num, resul))'''

'''num = int(input('Digite um valor para saber o seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c # aqui é feito primeiro a operação e depois a atribuição
    c -= 1 # cada vez que o loop for rodado o a variavel (c) sofre um decremento de -1
print('{}'.format(f))

Código do Guanabara usando o While
'''
num = int(input('Digite um número para saber o seu fatorial:'))
f = 1
c = num
print('{}! = '.format(num), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c += 1
print('{}'.format(f))