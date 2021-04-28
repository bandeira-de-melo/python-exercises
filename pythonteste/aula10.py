nome = str(input('Qual é o seu nome? '))
if nome == 'Naeme':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão comum!')
print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media >= 7:
    print('Sua nota foi boa, parabéns!')
else:
    print('Sua nota não foi suficiente, estude mais!')
print('Tenha um ótimo dia!')