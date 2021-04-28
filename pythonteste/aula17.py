'''num = [2, 5, 9, 1, 2]
num[1] = 3
num.append(7)
num.sort()
num.sort()
num.sort(reverse=True)
num.insert(1, 8)
num.pop(3)
num.remove(2)
if 3 in num:
    num.remove(3)
else:
    print('O número 3 não foi encontrado.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''

#for v in valores:
#    print(f'{v}...', end=' ')

#for c, v in enumerate(valores):
    #print(f'Na posição {c} foi encontrado o valor {v}')

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)'''

a = [2,4,8,7]
b = a# aqui foi feita um ligação entre a e b
b = a[:]# aqui foi feita uma cópia dos elementos de a para b
b [1] = 5# aqui foi inserido o valor 5 na posição 1
print(a)
print(b)