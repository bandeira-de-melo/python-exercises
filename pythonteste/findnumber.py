import random
num = random.randint(1, 5)
count = count2 = 0
sent = ('Not This Time :( Try again.',
        'That was close! Try again.',
        'Keep Trying.')
while True:
    guess = int(input('Guess a number between 1 and 5: '))
    if 1< guess >5:
        print('.' * 31)
        guess = int(input('The number must be between 1 and 5:'))
        count2 += 1
    count += 1
    if guess != num:
        print(random.choice(sent))
        print('.' * 31)
    else:
        print('=+' * 20)
        print(f'Bingo!!!')
        print(f'You tried {count} time(s)')
        if count2 > 0:
            print(f'{count2} number(s) out of range.')
        print('=+' * 20)
        option = str(input('Go again? [Y/N]')).strip()
        print('=+' * 20)
        if option in 'Nn':
            break
print('Bye!')
