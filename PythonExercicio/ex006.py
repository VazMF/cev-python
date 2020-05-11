#crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada
#operadores aritimetcios, aula 07
from time import sleep #importando sleep
print('\033[1;31m---DORBRO, TRIPLO E RAIZ---\033[m') #titulo
n = int(input('Insira um número: ' )) #pedindo o input do número
print('\033[34mPROCESSANDO...\033[m')
sleep(1)
print('\033[30mO DOBRO É\033[m: \033[31m{}\033[m'.format(n * 2)) #dobrando o número inserido
print('\033[30mO TRIPLO É\033[m: \033[31m{}\033[m'.format(n * 3)) #triplicando o número inserido
print('\033[30mA RAIZ QUADRADA É\033[m: \033[31m{:.1f}\033[m'.format(n ** 1/2)) #achando a raiz do número inserido


