frase = str(input('Digite sua palavra/frase para saber se ela é um palíndromo ')).strip().upper()
frasecut = frase.split()
junto = ''.join(frasecut)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print('{} é um palíndromo.'.format(frase))
else:
    print('{} não é um palíndromo'.format(frase))



