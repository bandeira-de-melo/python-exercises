count = 0
soma = 0
vals = []
while count < 10:
    n = int(input('Digite um valor: '))
    vals.append(n)
    count += 1
soma = sum(vals)
media = soma / 10
print(f'Os valores digitados foram: {vals}')
print(f'A média dos valores digitados é: {media}')
