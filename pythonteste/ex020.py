from random import shuffle
alu01 = input('Digite o nome do aluno 01: ')
alu02 = input('Digite o nome do aluno 02: ')
alu03 = input('Didite o nome do aluno 03: ')
alu04 = input('Digite o nome do aluno 04: ')
lista = [alu01, alu02, alu03, alu04]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
