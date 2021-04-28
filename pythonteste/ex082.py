listao = []
while True:
    listao.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()
    if resposta == 'N':
        break
print(f'Os números digitados {listao}')
listaPar = []
listaImpar = []
for i, v in enumerate(listao):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)
print(f'Os números pares na lista são: {listaPar}')
print(f'Os números ímpares na lista são: {listaImpar}')
