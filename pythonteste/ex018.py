import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o coseno de {:.2f}'.format(ang, coseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tang))
