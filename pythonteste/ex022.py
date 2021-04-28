nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('O nome completo sem espaço tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
nameup = nome.upper()
print('A letra A aparece {} vezes no nome.'.format((nameup.count('A'))))

