alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu Peso: '))
imc = peso / alt**2
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc <= 30:
    print('Acima do Peso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')