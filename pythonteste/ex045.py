from random import randrange
print('Vamos jogar Pedra, Papel e Tesoura')
jogador = int(input('\n 1 = tesoura \n 2 = papel \n 3 = pedra \n'))
maquina = randrange(1,3)
if jogador == 1 and maquina == 2:
    print('Voce (tesoura) ganhou da maquina (papel)')
elif jogador == 1 and maquina == 3:
    print('Voce (tesoura) perdeu da maquina (pedra)')
elif jogador == 2 and maquina == 1:
    print('Voce (papel) perdeu da maquina (tesoura)')
elif jogador == 2 and maquina == 3:
    print('Voce (papel) ganhou da maquina (pedra)')
elif jogador == 3 and maquina == 2:
    print('Voce (pedra) perdeu da maquina (papel)')
elif jogador == 3 and maquina == 1:
    print('Voce (pedra) ganhou da maquina (tesoura)')
elif jogador == maquina:
    print('Deu em empate.')