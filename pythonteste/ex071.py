valor = int(input('Qual o valor que você deseja sacar? R$'))
total = valor
céd = 50
qtd_céd = 0
while True:
    if total >= céd:
        total -= céd #enquato o total for maior ou igual ao valor da cédula ele vai subitrair esse valor do total
        qtd_céd += 1 #a cada cédula subitraida do total ele vai contar uma unidade
    else:
        if qtd_céd > 0:
            print(f'Foram sacadas {qtd_céd} de R$ {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        qtd_céd = 0
        if total == 0:
            break
print('Fim.')






