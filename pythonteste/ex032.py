from datetime import date
ano = int(input('Digite um ano no formato xxxx para saber se ele é bissexto ou não. Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano \33[35mbissexto\33[m'.format(ano))
else:
    print('{} não é um ano \33[35mbissexto.\33[m'.format(ano))

