idades = 0
media_id = float(0)
caixa1 = 0
qtd = 0
for p in range(1, 5):
    nome = (input('Digite o nome da pessoa {}: '.format(p))).strip()
    idade = int(input('Digite a idade da pessoa {}: '.format(p)))
    sexo = str(input('Digite o sexo F ou M da pessoa {}: '.format(p))).strip().upper()
    idades += idade
    if sexo == 'M':
        if idade > idadevelho:
            idadevelho = idade
            nome_velho = nome
    if sexo == 'F':
        if idade < 20:
            qtd += 1
media_id = idades / 4
print('A media de idade de todas as pessoas é: {} anos'.format(media_id))
print('Idade do homem mais velho: {}'.format(nome_velho))
print('O número de mulheres abaixo dos 20 anos é: {}'.format(qtd))