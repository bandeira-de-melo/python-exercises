'''valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valores)
menor = min(valores)
print('-'*30)
print(f'O maior valor digitado foi: {maior} na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=' ')
print(f'\nO menor valor digitado foi: {menor} na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=' ')'''
