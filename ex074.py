from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1,10))
print('Os valores sortiados foram: ',end='')
for n in numeros:
    print(f'{n} ',end='')
print(f'\nO maior valor sortiado foi {max(numeros)}')
print(f'O menor valor sortiado foi {min(numeros)}')
