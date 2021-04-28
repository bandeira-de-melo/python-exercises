velo = float(input('Digite a velocidade do carro: '))
multa = float((velo - 80) * 7)
kmexce = float(velo - 80)
if velo > 80:
    print('O carro excedeu a velocidade limite em {} Km/h. O valor da multa é R$ {:.2f}'.format(kmexce, multa))
else:
    print('O carro está dentro do limite de velocidade')
    