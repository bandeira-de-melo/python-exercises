#Meu código
'''matriz = [[], [], []]
c = c2 = 0
while c < 3:
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c, i}]: ')))
    c += 1
while c2 < 3:
    for i in range(0, 3):
        print(f'[{matriz[c2][i]}] ', end='')
        if i > 1:
            print('\n')
    c2 += 1'''

#Código Guanabara
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
