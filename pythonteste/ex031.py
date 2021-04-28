viagemkm = float(input('Digite a quantidade de Km percorridos na viagem: '))
preço = viagemkm * 0.50 if viagemkm <= 200 else viagemkm * 0.45
print('A viagem vai custar \33[32mR${:.2f}\33[m'.format(preço))
mensagem = print('Sua viagem teve tarifa normal') if viagemkm <= 200 else print('Sua viagem teve tarifa promocional')
print('\33[1;36mTenha uma boa viagem!\33[m')

