sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    aumento = (sal * 10)/100
else:
    aumento = (sal * 15)/100
print('O valor do aumento para esse funcionário é R$ {:.2f}'.format(aumento))