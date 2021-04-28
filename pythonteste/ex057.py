sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
while (sexo != 'M' and sexo != 'F'):
    sexo = str(input('Por favor, digite o sexo da pessoa novamente. Sendo [F ou M]:')).strip().upper()[0]

