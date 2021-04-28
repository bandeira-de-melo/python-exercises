'''frase = input('Digite uma frase com alguma palavra entre parênteses: ')
x = frase.find('(')
if x != -1:
    for i in range(x, len(frase)):
        y = frase.find(')')
if y != -1:
    print(f'Os parenteses da frase, {frase}, estão posicionados corretamente.')
elif y == -1:
    print(f'A ordem dos parênteses na frase, {frase}, está incorreta.')'''
frase = input('Digite uma expressão com parenteses: ')
count = 0
while True:
    for i in range(len(frase)):
        x = frase.find('(')
        if x != -1:
            count += 1
        

