#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. depois disso mostre a listagem de números
#gerados também indique o menor e o maior valor que estão na lista.
from random import randint
print('-' * 40)
print('{:^40}'.format('SORTEIO EM TUPLAS'))
print('-' * 40)
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi: {max(num)} ')
print(f'O menor valor sorteado foi: {min(num)}')
print('-' * 40)
