opc = 4
opera = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
opc = int(input('Escolha uma opção: \n [1] adição\n [2] multiplicar\n [3] Maior\n [4] novos números\n [5] Sair:\n'))
while opc != 5:
    if opc == 1:
        opera = num1 + num2
        print('O resultado da adição é: {}'.format(opera))
        print('=*=' * 10)
        opc = int(input('Escolha uma opção: \n [1] adição\n [2] multiplicar\n [3] Maior\n [4] novos números\n [5] Sair:\n'))
    elif opc == 2:
        opera = num1 * num2
        print('O resultado da multiplicação é {}'.format(opera))
        print('=*=' * 10)
        opc = int(input('Escolha uma opção: \n [1] adição\n [2] multiplicar\n [3] Maior\n [4] novos números\n [5] Sair:\n'))
    elif opc == 3:
        if num1 > num2:
            maior = num1
            print('O mario número é {}'.format(num1))
            opc = 4
            print('=*=' * 10)
        if num2 > num1:
            maior = num2
            print('O maior número é {}'.format(num2))
            opc = 4
            print('=*=' * 10)
        if num1 == num2:
            print('Os dois números são iguais')
            opc = int(input('Pressione 4 para inserir novos números.'))
            print('=*='*10)
    elif opc == 4:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            opc = int(input('Escolha uma opção: \n [1] adição\n [2] multiplicar\n [3] Maior\n [4] novos números\n [5] Sair:\n'))
    elif opc == 5:
        opc = 5
    else:
        print('Opção inválida')
print('Fim do programa. Volte Sempre!')
'''n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opc = 0
soma = 0
produto = 0
while opc != 5:
    print(    [1] adição
    [2] multiplicação
    [3] maior
    [4] novos valores
    [5] sair)
    opc = int(input('Qual é sua opção? '))
    if opc == 1:
        soma = n1 + n2
        print('O resultado da adição é? {}'.format(soma))
        print('=-=' * 10)
    elif opc == 2:
        produto = n1 * n2
        print('O resultado da multiplicação é: {}'.format(produto))
        print('=-=' * 10)
    elif opc == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é: {}'.format(n1, n2, maior))
            print('=-=' * 10)
        else:
            maior = n2
            print('O maior número entre {} e {} é: {}'.format(n1, n2, maior))
            print('=-=' * 10)
    elif opc == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida')
        print('=-=' * 10)'''