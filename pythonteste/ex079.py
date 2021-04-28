lista = []
saida = 'S'
num = int(input('Digite um valor: '))
while True:
    if num in lista:
        num = int(input('Valor já adicionado. Digite um valor diferente: '))
    else:
        lista.append(num)
        saida = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if saida != 'S':
            break
        num = int(input('Digite um valor: '))
print('-='*30)
print(f'Os números digitados foram: {sorted(lista)}')


