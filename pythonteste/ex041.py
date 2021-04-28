from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Idade: {}'.format(idade))
    print('Categoria Mirim')
elif idade <= 14:
    print('Idade: {}'.format(idade))
    print('Categoria Infatil')
elif idade <= 19:
    print('Idade: {}'.format(idade))
    print('Categoria Junior')
elif idade <= 20:
    print('Idade: {}'.format(idade))
    print('Categoria Senior')
else:
    print('Idade: {}'.format(idade))
    print('Categoria Master')
