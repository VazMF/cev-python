#crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada
#operadores aritimetcios, aula 07
from time import sleep #importando sleep
from math import sqrt #importando a funcao pra calcular a raiz quadrada
print('\033[34m---DORBRO, TRIPLO E RAIZ---\033[m') #titulo
n = int(input('Insira um número: ' )) #pedindo o input do número para a variavel n
print('\033[34mPROCESSANDO...\033[m') #printo do processamento para simular loading
sleep(1) #sleep de 1s
print(f'O DOBRO É: \033[34m{n * 2}\033[m') #dobrando o número inserido
print(f'O TRIPLO É: \033[34m{n * 3}\033[m') #triplicando o número inserido
print(f'A RAIZ QUADRADA É: \033[34m{sqrt(n):.1f}\033[m') #achando a raiz do número inserido
