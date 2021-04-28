quant = maior = menor = num = soma = media = 0
resp = ('')
while resp != 'N':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant += 1
    if quant == 1:
        menor = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja adicionar mais um valor? [S/N]')).upper().strip()[0]
media = soma/quant
print('A quantidade de números digitados foi {} e a média é {}'.format(quant, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))
