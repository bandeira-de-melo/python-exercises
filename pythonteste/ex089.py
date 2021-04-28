turma = []
aluno = []
notas = []
c = 0
while True:
    aluno.append(str(input('Nome: ')))
    n1 = float(input(f'Nota 1:'))
    n2 = float(input(f'Nota 2:'))
    media = (n1 + n2) / 2
    notas.append(n1)
    notas.append(n2)
    aluno.append(notas[:])
    aluno.append(media)
    turma.append(aluno[:])
    aluno.clear()
    notas.clear()
    resp = str(input('Continuar cadastro? [S/N]')).upper().strip()
    if resp == 'N':
        break
print('No  Nome   Média')
for t in range(0, len(turma)):

    print(t, end='   ')
    print(turma[t][0], end='  ')
    print(turma[t][2])
print('-'*30)
while True:
    opç = int(input('Mostrar nota de qual aluno? 999 para sair. '))
    if opç == 999:
        break
    else:
        print(f'As notas de {turma[opç][0]}', end='')
        print(f' são: {turma[opç][1]}')
        print('-'*30)







