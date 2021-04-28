nums = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro número: ')))
cont = 0
print(f'Voce digitou os valores: {nums}')
print(f'O número 9 apareceu {nums.count(9)} vezes na lista.')
if 3 in nums:
    print(f'O número 3 aparece na posição {nums.index(3)+1} da lista')
else:
    print(f'O número 3 não apareceu nenhuma posição da lista.')
print('Os números pares digitados na lista foram: ', end='')
for c in nums:
    if c % 2 == 0:
        print(c, end= ' ')


