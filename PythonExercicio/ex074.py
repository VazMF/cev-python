#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. depois disso mostre a listagem de números
#gerados também indique o menor e o maior valor que estão na lista.
from random import randint
print('-' * 40)
print(f'{"SORTEIO EM TUPLAS":^40}') #titulo
print('-' * 40)
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10)) #sorteia 5 valores de 1 a 10 em uma tupla
print(f'Os valores sorteados foram: ', end='') #print para informar os valores (sem quebrar linha)
for n in num: #reprticao para cada numero na tupla num
    print(f'{n} ', end='') #print formatado com o numero
print(f'\nO maior número sorteado foi: {max(num)}') #quebra de linha e print do vmaior valor com max
print(f'O menor valor sorteado foi: {min(num)}') #print do menor valor com min
print('-' * 40)
