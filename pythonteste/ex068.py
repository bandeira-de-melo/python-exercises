from random import randint
quant = 0
print('Vamos Jogar par ou ímpar: ')
print('-='*10)
while True:
    eu = int(input('Diga um valor:'))
    pc = randint(1,9)
    soma = eu + pc
    if soma % 2 == 0:
        parimp = 'P'
        resul = 'DEU PAR!'
    else:
        parimp = 'I'
        resul = 'DEU ÍMPAR!'
    escolha = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    if escolha == parimp:
        print(f'Você jogou {eu} e o computador {pc}. Total de {soma} {resul}')
        print('Você venceu!')
        print('Vamos Jogar Novamente!')
        print('-=0' * 10)
        quant += 1
    else:
        print(f'Você jogou {eu} e o computador {pc}. Total de {soma} {resul}')
        print('Você perdeu!')
        print('Game Over!')
        print(f'Você venceu {quant} vez(es)')
        break

