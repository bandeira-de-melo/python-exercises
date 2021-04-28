geral = [[], []]

for n in range(8):
    nums = int(input('Digite um número'))
    if nums % 2 == 0:
        geral[0].append(nums)#coloca num dentro da sublista de indice 0 na lista geral
    elif nums % 2 == 1:
        geral[1].append(nums)
print(f'Na lista de números pares temos: {sorted(geral[0])}')
print(f'Na lista de números ímpares temos:{sorted(geral[1])}')


