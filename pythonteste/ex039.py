from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
anosfalta = 18 - idade
anospass = idade - 18
if idade < 18:
    print('Voce ainda não está na idade de alistamento, faltam {} anos.'.format(anosfalta))
elif idade > 18:
    print('Voce já passou do prazo de alistamento, está atrasado em {} anos.'.format(anospass))
else:
    print('Voce pode se alistar agora.')
