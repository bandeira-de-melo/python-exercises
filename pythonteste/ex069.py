cont_idade = cont_sexo = menos20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('-=' * 10)
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_sexo += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Continuar cadastro? [S/N]: ')).strip().upper()[0]
    print('-=' * 10)
    if saida == 'N':
        break
print(f'{cont_idade} pessoa(s) têm mais de 18 anos.')
print(f'Foram cadastrados {cont_sexo} homen(s).')
print(f'{menos20} mulher(es) têm menos de 20 anos.')