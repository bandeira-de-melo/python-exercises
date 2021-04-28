sal = float(input('Qual o salário do funcionário? R$'))
aumen = int(input('De quantos por cento foi seu aumento? '))
valoraumen = sal * aumen / 100
salaumen = sal + valoraumen
print('O salário do funcionário com {}% de aumento é R${}'.format(aumen, salaumen))