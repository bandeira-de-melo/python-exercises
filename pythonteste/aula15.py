'''n = s = 0
while n != 999:
    n = int(input('Digite um número:'))
    s += n
print(f'a soma dos números é: {s}')
print('Acabou')'''
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print(f'a soma dos números é: {s}')
print('Acabou')