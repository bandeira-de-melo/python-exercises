valor = float(input('Digite o valor do produto: '))
opçpag = float(input('Escolha a opção de pagamento \n 1=Dinheiro/chegue \n 2= Débito \n 3= 2x cartão \n 4= 3x Cartão:\n '))

if opçpag == 1:
    desc = valor*10/100
    total = valor - desc
    print('Você ganhou 10% de desconto, o total a ser pago é R${}'.format(total))
elif opçpag == 2:
    desc = valor*5/100
    total = valor - desc
    print('Você ganhou 5% de desconto, o total a ser pago é R${}'.format(total))
elif opçpag == 3:
    print('Essa forma de pagamento não inclui descontos, total a ser pago R${}'.format(valor))
else:
    juros = valor*20/100
    total = valor + juros
    print('Será acrescentado 20% de juros a essa forma de pagamento, total a ser pagoR${}'.format(total))
