aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média do aluno: '))
if aluno['media'] >= 7:
    print(f'{aluno["nome"]} está aprovado.')
else:
    print(f'{aluno["nome"]} está reprovado.')
