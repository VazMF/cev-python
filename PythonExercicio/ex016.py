#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#aula 08, utilizando módulos
from math import trunc
from time import sleep
print('\033[1;31m---PARTE INTEIRA---\033[m') #titúlo
num = float(input('Digite um número real: ')) #input do número real
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('A parte inteira de \033[32m{}\033[m é \033[32m{}\033[m'.format(num, trunc(num))) #pegando a parte inteira do input por meio da função trunc e mostrando o resultado

