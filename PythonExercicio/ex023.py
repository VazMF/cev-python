#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
from time import sleep
print('\033[31m---SEPARANDO DIGÍTOS---\033[m') #titúlo
num = int(input('\033[30mInforme um numero:\033[m ')) #input do número que vai ser separado
U = num // 1 % 10 #separando unidade pela divisão inteira
D = num // 10 % 10 #dezena por divisão inteira
C = num // 100 % 10 #centena por divisãointeira
M = num // 1000 % 10 #milhar por divisão inteira
print('\033[1;32mANALISANDO O NÚMERO...\033[m'.format(num))
sleep(1)
print('\033[30mUnidade:\033[m \033[32m{}\033[m'.format(U)) #mostrando a unidade
print('\033[30mDezena:\033[m \033[32m{}\033[m'.format(D)) #mostrando a dezena
print('\033[30mCentena:\033[m \033[32m{}\033[m'.format(C)) #mostrando a centena
print('\033[30mMilhar:\033[m \033[32m{}\033[m'.format(M)) #mostrando o milhar
print('\033[31m-\033[m' * 23) #fim


