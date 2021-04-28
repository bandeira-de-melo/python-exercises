total = cont = preço = mais_mil = 0
print('-' * 10)
print('Lojão Barratão')
print('-' * 10)
while True:
    nome = str(input('Qual o nome do Produto: ')).strip()
    preço = float(input('Qual o preço do produto? '))
    print('-=' * 10)
    cont += 1
    total += preço
    if preço >= 1000:
        mais_mil += 1
    if cont == 1:
        menor_preço = preço
        menor_nome = nome
    if preço < menor_preço:
        menor_preço = preço
        menor_nome = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar comprando? [S/N]')).strip().upper()[0]
        print('-=' * 10)
    if resp == 'N':
        break
print(f'O valor total da compra é: R${total}')
print(f'{mais_mil} produtos custam mais de R$ 1.000,00')
print(f'Produto mais barato: {menor_nome}')

