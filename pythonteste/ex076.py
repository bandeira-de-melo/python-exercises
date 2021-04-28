listagem = ('Lápis', 1.25, 'Caderno', 22, 'Tesoura', 3.50, 'Borracha', 1.2)
print('-'*42)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('-'*42)
for x in range(0, len(listagem)):
    if x % 2 == 0:
        print(f'{listagem[x]:.<30}R$', end='')
    else:
        print(f'R$ {listagem[x]:>7.2f}')

