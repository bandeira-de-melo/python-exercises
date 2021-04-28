import math
cat1 = int(input('Digite a medida do cateto oposto: '))
cat2 = int(input('Digite a medida do cateto adjacente: '))
hipo = math.hypot(cat1, cat2)
print('A medidada da hipotenusa é: {:.2f}m'.format(hipo))
