#Meu Código
'''num = int(input('Digite um o primeiro valor da P.A: '))
num_ini = num
rz = int(input('Digite a razão da pa: '))
lim = int(input('Digite o número de termos que deseja ver:'))
elem = 0
print('Os {} primeiros elementos da P.A são: '.format(lim), end='')
while elem < lim and lim != 0:
    print(num, end='')
    print((' + ' if elem < (lim - 1) else ''), end='')
    num = num + rz
    elem += 1
    if elem == lim:
        mais = int(input('\nQuantos termos a mais vc quer ver? Digite 0 para sair.'))
        if mais != 0:
            lim += mais
            elem = 0
            num = num_ini
print('=-' * 10)
print('Fim. Volte Sempre!')'''

#Código Guanabara
primeiro = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
termo = primeiro
cont = 1
mais = 10
total = 0
elementos = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
        elementos += 1
    print('Pausa')
    mais = int(input('Quantos termos ainda deseja ver? Digite 0 para sair.'))
print('FIM. o total de elementos mostrado foi {}'.format(elementos))

