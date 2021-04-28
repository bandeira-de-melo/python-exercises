resp = 'S'
listao = []
cont = 0
while resp == 'S':
    listao.append(int(input('Digite um valor: ')))
    cont += 1
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
ordem = list(sorted(listao))
inverso = list(reversed(ordem))
print('-='*30)
print(f'A quantidade de números digitados foi: {cont}')
print(f'Os números em ordem decrescente são: {inverso}')
if 5 in listao:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')