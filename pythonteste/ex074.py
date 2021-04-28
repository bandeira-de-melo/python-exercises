from random import randint
nums = ((randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)))
print(f'Os números sorteados são: {nums}')
print(f'O maior número é {max(nums)}')
print(f'O menor número é {min(nums)}')