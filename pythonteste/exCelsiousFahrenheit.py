nomeDog = str(input('Digite o nome do doguinho: '))
dogAge = float(input('Digite a idade do doguinho: '))
idade1 = 0
idhum1 = 10.5
idhum2 = 4
cont = 0
while cont < dogAge:
    if cont < 2:
        idade1 += idhum1
    else:
        idade1 += idhum2
    cont += 1
print(f'{nomeDog} tem idade humana de: {idade1}')