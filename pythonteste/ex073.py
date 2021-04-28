times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Atlético-PR', 'Bragantino',
         'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('Os times em ordem alfabética são: ', sorted(times))
print(f'O Palmeiras está na posição: {times.index("Palmeiras")+1}')
