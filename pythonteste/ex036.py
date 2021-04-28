print('Bem vindo ao programa de financimento Meu Barraco!')
valcasa = float(input('Digite o valor do imóvel: '))
salcomp = float(input('Digite o salário do comprador:'))
anos = int(input('Em quanto anos o imóvel será pago? '))
numparcelas = anos * 12
valprest = valcasa / numparcelas
porcentsal = (salcomp*30)/100
if porcentsal < valprest:
    print('Infelizmente, o seu salário é insuficiente para o valor da parcela.')
else:
    print('Parabes! A compra do seu imóvel foi aprovada!')
print('Tenha um ótimo dia')