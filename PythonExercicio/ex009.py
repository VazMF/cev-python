#faça um programa que leia um número inteiro e mostre sua tabuada
from time import sleep #import do sleep
print('\033[1;31m-------TABUADA-------\033[m') #titúlo
n = int(input('Insira um número: ')) #input do numero na variavel num
print(f'{n} x 1 \033[31m=\033[m {n*1}') #print da visualizacao e multiplicacao dos numeros
print(f'{n} x 2 \033[31m=\033[m {n*2}')
print(f'{n} x 3 \033[31m=\033[m {n*3}')
print(f'{n} x 4 \033[31m=\033[m {n*4}')
print(f'{n} x 5 \033[31m=\033[m {n*5}')
print(f'{n} x 6 \033[31m=\033[m {n*6}')
print(f'{n} x 7 \033[31m=\033[m {n*7}')
print(f'{n} x 8 \033[31m=\033[m {n*8}')
print(f'{n} x 9 \033[31m=\033[m {n*9}')
print(f'{n} x 10 \033[31m=\033[m {n*10}')
print('\033[31m-\033[m'*22) #print do final
