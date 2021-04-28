nome = str(input('Qual é o seu nome? '))
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Naeme Sandro':
    print('Belo nome feminino')
else:
    print('Seu nome é bem comum')
print('Tenha um bom dia, {}'.format(nome))