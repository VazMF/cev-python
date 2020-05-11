#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
from time import sleep
print('\033[31m---PAR OU IMPÁR?---\033[m')
n = int(input('Digite um número: '))#capta o número digitado pelo usuário
print('\033[33mPROCESSANDO...\033[m')
sleep(1)
if n%2==0: #verifica se o número é par
    print('O número {} é \033[4;33mPAR\033[m.'.format(n))#mensagem que aparece caso o número for par
else:
    print('O número {} é \033[4;33mIMPÁR\033[m.'.format(n))#mensagem caso o número seja ímpar
print('\033[31m-\033[m' * 19)

