
alimentos = ('sopa', 'leite', 'queijo', 'cebola','batata')
print('-'*32)
print(f'{"ALIMENTOS":^32}')
print('-'*32)
for i in alimentos:
    print(f'\nNa palavra {i.upper()} temos: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n')
print('-'*32)

