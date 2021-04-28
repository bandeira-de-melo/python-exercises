r1 = float(input('Digite a medida primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da terceira reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('E possivel formar um triangulo.')
    if r1 == r2 == r3:
        print('Esse é um triângulo Equilátero.')
    elif r1 != r2 != r3 !=r1:
        print('Esse é um triângulo Escaleno')
    else:
        print('Esse é um triângulo Isósceles.')
else:
    print('Não é possível formar o triangulo.')
