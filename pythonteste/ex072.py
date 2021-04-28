nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
#número = int(input('Digite um número entre 0 e 20: '))
#while not número > -1 or not número < 20:
#    número = int(input('Digite um número entre 0 e 20: '))
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if 0 <= número <= 20: # igual a if número >= 0 and número >= 20
        break
número = nums[número]
print(número)
