km = float(input('Quantos Km o carro rodou? '))
dias = float(input('Quantos dias o carrou ficou alugado? '))
precokm = float(0.15)
precodia = float(60)
totalpagar = (km * precokm) + (dias * precodia)
print('O valor total a ser pago é: R$', totalpagar)
