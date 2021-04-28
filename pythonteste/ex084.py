clientes = []
dados = []
pesos = []
maisPesados = []
maisLeves = []
resp = ''
cont = 0
while resp != 'N':
    dados.append(str(input('Digite o nome do cliente: ')))
    dados.append(float(input('Digite o peso do cliente: ')))
    clientes.append(dados[:])# cria uma cópia do que vem de dados para dentro de clientes
    dados.clear()
    cont += 1
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()
for i, v in enumerate(clientes):
    pesos.append(clientes[i][1])#separar pesos
maxPeso = max(pesos)
minPeso = min(pesos)
for i, v in enumerate(clientes):
    if maxPeso in (clientes[i]):# cada vez que passar vai procurar pelo valor de da variavel maxpeso dentro da da sublista de indice i na lista clientes
        maisPesados.append(clientes[i][0])#vai gua
    if minPeso in (clientes[i]):
        maisLeves.append(clientes[i][0])

print(f'Você cadastrou {cont} pessoas.')
print(f'O maior peso cadastrado foi {maxPeso}Kg. Peso de {maisPesados[:]}')

'''#print(i, v)
    if i == 0:
        print('Ola')
    maisPesados.append(clientes[0])
    if maisPesados([0][1]) < v[1]:
        maisPesados[0] = v
    #x = clientes.index(c)
    #pesos.append(clientes[x][1])

print(pesos)
print(clientes[0])
print(maisPesados)'''

