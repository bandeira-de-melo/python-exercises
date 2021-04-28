from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {} pessoa:'.format(c)))
    idade = date.today().year - ano
    if idade < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} Menores de idade'.format(menor))
print('{} Maiores de idade.'.format(maior))