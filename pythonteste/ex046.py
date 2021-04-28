import time
import emoji
print('A contagem regressiva começou:')
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize(':fireworks:'))
