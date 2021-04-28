'''listpeso = []
for c in range(1, 6):
    peso = int(input('Digite o peso da pessoa {}: '.format(c)))
    listpeso.append(peso)
listordem = sorted(listpeso)
print('O maior peso é {}Kg'.format(listordem[5]))
print('O menor peso é {}Kg'.format(listordem[0]))'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Leia o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))


