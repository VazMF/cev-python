#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc #import do trunc
print('\033[35m-------PARTE INTEIRA-------\033[m') #titúlo
num = float(input('Digite um número real: ')) #input do número real na variavel num
print(f'A parte inteira de \033[35m{num}\033[m é \033[35m{trunc(num)}\033[m') #pegando a parte inteira do input por meio da função trunc e mostrando o resultado
