#faça um programa que leia um número inteiro e mostre sua tabuada
#operadores aritimeticos, aula 07
from time import sleep
print('\033[1;31m---TABUADA---\033[m') #titúlo
n = int(input('\033[1;30mInsira um número\033[m: ')) #input do num
print('\033[32mPROCESSANDO...\033[m')
sleep(1)
print('{} x 1 \033[31m=\033[m {}'.format(n, n*1))
print('{} x 2 \033[31m=\033[m {}'.format(n, n*2))
print('{} x 3 \033[31m=\033[m {}'.format(n, n*3))
print('{} x 4 \033[31m=\033[m {}'.format(n, n*4))
print('{} x 5 \033[31m=\033[m {}'.format(n, n*5))
print('{} x 6 \033[31m=\033[m {}'.format(n, n*6))
print('{} x 7 \033[31m=\033[m {}'.format(n, n*7))
print('{} x 8 \033[31m=\033[m {}'.format(n, n*8))
print('{} x 9 \033[31m=\033[m {}'.format(n, n*9))
print('{} x 10 \033[31m=\033[m {}'.format(n, n*10))
print('\033[31m-\033[m'*12)
