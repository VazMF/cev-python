#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
from time import sleep #import do sleep
print('\033[32m---SEPARANDO DIGÍTOS---\033[m') #titúlo
num = int(input('Informe um numero: ')) #input do número que vai ser separado na variavel num
U = num // 1 % 10 #separando unidade pela divisão inteira e colocando na variavel U
D = num // 10 % 10 #dezena por divisão inteira e colocando na variavel D
C = num // 100 % 10 #centena por divisãointeira e colocando na variavel C
M = num // 1000 % 10 #milhar por divisão inteira e colocando na variavel M
print('\033[32mANALISANDO O NÚMERO...\033[m'.format(num)) #print para simular loading
sleep(1) #sleep
print(f'Unidade: \033[32m{U}\033[m') #mostrando a unidade
print(f'Dezena: \033[32m{D}\033[m') #mostrando a dezena
print(f'Centena: \033[32m{C}\033[m') #mostrando a centena
print(f'Milhar: \033[32m{M}\033[m') #mostrando o milhar
print('-' * 23) #fim


